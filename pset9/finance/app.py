import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Obtain list of symbols and shares
    portfolio = db.execute("SELECT * FROM portfolio")

    # Check to make sure user has made a purchase
    if not portfolio:
        return apology("You have no purchases, click buy", 200)

    # Obtain user's cash
    obtain_cash = db.execute("SELECT cash FROM users where id=?", session["user_id"])
    cash = obtain_cash[0]['cash']

    # Running total using cash plus each symbols share value
    total = cash

    # Obtain values for each symbol with lookup function
    for symbol in portfolio:
        price = lookup(symbol['symbol'])['price']
        name = lookup(symbol['symbol'])['name']
        share_total = symbol['shares'] * price
        symbol['price'] = price
        symbol['share_total'] = share_total
        symbol['name'] = name
        total += share_total

    # Render template with values
    return render_template("index.html", portfolio=portfolio, cash=cash, price=price, name=name, total=total, share_total=share_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # Make sure POST request
    if request.method == "POST":

        # Check that symbol was entered
        if not request.form.get("symbol"):
            return apology("must enter stock symbol")

        # Obtain quote from lookup function
        quote = lookup(request.form.get("symbol"))

        # Check for valid quote
        if quote is None:
            return apology("symbol not valid")

        # Check that shares number was entered
        shares = int(request.form.get("shares"))
        if not shares:
            return apology("must enter number of shares to buy")

        # Check number of shares is positive integer
        if shares < 1:
            return apology("number of shares to buy must be positive")

        # Check if shares amount is fractional
        if not shares.is_integer():
            return apology("number of shares must be whole number)

        # Obtain users current amount of cash available
        cash_list = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = cash_list[0]["cash"]

        # Calculate cost of purchase
        cost = int(request.form.get("shares")) * quote['price']

        # Compare cash available to cost of purchase
        if cost > cash:
            return apology("not enough funds for purchase")

        # Update user cash if transaction goes through
        db.execute("UPDATE users SET cash=? WHERE id=?", cash-cost, session["user_id"])

        # Add purchase to transactions table
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)",
                   session["user_id"], quote['symbol'], request.form.get("shares"), quote['price'], datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

        # Update user's portfolio with purchase

        # Obtain number of shares already purchased
        shares = db.execute("SELECT shares FROM portfolio WHERE symbol=?", quote['symbol'])

        # If no shares, add stock to portfolio and update shares amount
        if not shares:
            db.execute("INSERT INTO portfolio (symbol, shares) VALUES (?, ?)", quote['symbol'], int(request.form.get("shares")))

        # If already own symbol, update shares amount with new purchase
        else:
            db.execute("UPDATE portfolio SET shares=? WHERE symbol=?",
                       shares[0]["shares"]+int(request.form.get("shares")), quote['symbol'])

        # Render template for index when finished
        return redirect("/")

    # Check for GET request and redirect
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Get transactions for user
    transactions = db.execute("SELECT symbol, shares, price, date FROM transactions WHERE user_id=?", session["user_id"])

    # Check for transactions
    if not transactions:
        return apology("you have no transactions so far")

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # Check to make sure requested submitted via POST
    if request.method == "POST":

        # Make sure user inputted something
        if not request.form.get("symbol"):
            return apology("must enter stock symbol")

        # Obtain quote from lookup function
        quote = lookup(request.form.get("symbol"))

        # Check for valid quote
        if quote is None:
            return apology("symbol not valid", 400)

        # Render quoted.html if valid quote
        else:
            return render_template("quoted.html", quote=quote)

    # Redirect for GET request
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password and confirmation were submitted
        elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("must provide password", 400)

        # Ensure that password and confirmation match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password and confirmation do not match", 400)

        # Create hash of user's password to store in db
        pwhash = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)

        # Store new user in db
        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), pwhash)
            return redirect('/')
        except:
            return apology("username is already registered", 400)

    # User reached route via GET redirect to register
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # Make sure POST request
    if request.method == "POST":

        # Check that symbol was entered
        if not request.form.get("symbol"):
            return apology("must enter stock symbol")

        # Obtain quote from lookup function
        quote = lookup(request.form.get("symbol"))

        # Check for valid quote
        if quote is None:
            return apology("symbol not valid")

        # Check that shares number was entered
        if not request.form.get("shares"):
            return apology("must enter number of shares to buy")

        # Check number of shares is positive integer
        if int(request.form.get("shares")) < 1:
            return apology("number of shares to sell must be positive")

        # Obtain number of shares already purchased
        shares = db.execute("SELECT shares FROM portfolio WHERE symbol=?", quote['symbol'])

        # Check that user isn't selling more shares than they own
        if int(request.form.get("shares")) > shares[0]["shares"]:
            return apology("cannot sell more shares than currently own")

        # Obtain users current amount of cash available
        cash_list = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = cash_list[0]["cash"]

        # Calculate proceeds of sale
        proceeds = int(request.form.get("shares")) * quote['price']

        # Update user cash if transaction goes through
        db.execute("UPDATE users SET cash=? WHERE id=?", cash+proceeds, session["user_id"])

        # Add sale to transactions table
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)",
                   session["user_id"], quote['symbol'], -int((request.form.get("shares"))), quote['price'], datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

        # Update shares amount with sale
        db.execute("UPDATE portfolio SET shares=? WHERE symbol=?",
                   shares[0]["shares"]-int(request.form.get("shares")), quote['symbol'])

        # Render template for index when finished
        return redirect("/")

    # Check for GET request and redirect
    else:
        # Get user portfolio to load drop-down menu
        portfolio = db.execute("SELECT symbol FROM portfolio")
        return render_template("sell.html", portfolio=portfolio)
