-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Check the crime scene reports table for the date of July 28, 2021 and Humphrey Street
SELECT description, id
  FROM crime_scene_reports
 WHERE year = 2021
   AND month = 07
   AND day = 28
   AND street = "Humphrey Street";

-- Obtained crime scene id of 295.  Let's check bakery logs.
  SELECT id, activity, license_plate, hour, minute
    FROM bakery_security_logs
   WHERE year = 2021
     AND month = 07
     AND day = 28
     AND hour = 9  AND minute > 13 OR hour = 10 AND minute < 17
ORDER BY hour, minute;

-- Let's run a list of all the people whose license plate was seen at the bakery between 9:14 and 10:20
SELECT id, name, license_plate
  FROM people
 WHERE license_plate
    IN (
        SELECT license_plate
        FROM bakery_security_logs
        WHERE year = 2021
        AND month = 07
        AND day = 28
        AND hour = 9  AND minute > 13 OR hour = 10 AND minute < 17
        ORDER BY hour, minute
);

-- Vanessa (id = 221103) entered at 9:15 and left at 10:16. Let's check her out.
SELECT transcript FROM interviews WHERE name = "Vanessa";

-- There were no interviews with Vanessa.  Let's check the interviews with anyone else at the bakery that day.
SELECT name, transcript
  FROM interviews
 WHERE year = 2021
   AND month = 07
   AND day = 28;

-- This gives us interviews with 4 people: Emma (bakery owner), Raymond, Eugene, and Ruth.  Ruth saw the thief leave the bakery within 10 minutes of the theft.  Let's check the logs
SELECT id, name, license_plate
  FROM people
 WHERE license_plate
    IN (
        SELECT license_plate, hour, minute, activity
        FROM bakery_security_logs
        WHERE year = 2021
        AND month = 07
        AND day = 28
        AND hour = 10 AND minute > 14 AND minute < 26
        AND activity = "exit"
);

-- List of suspects: Vanessa (top suspect), Barry, Iman, Sofia, Luca, Diana, Kelsey, Bruce.
-- Let's check Eugene's tip that he saw the thief withdrawing money at the ATM on Leggett Street the morning of the crime.
SELECT id, account_number, atm_location, transaction_type, amount
FROM atm_transactions
WHERE year = 2021
AND month = 07
AND day = 28
AND atm_location = "Leggett Street"
AND transaction_type = "withdraw";

-- This gives us 8 account numbers.  Let's cross reference with bank accounts
SELECT person_id
FROM bank_accounts
WHERE account_number IN (
    SELECT account_number
    FROM atm_transactions
    WHERE year = 2021
    AND month = 07
    AND day = 28
    AND atm_location = "Leggett Street"
    AND transaction_type = "withdraw");

-- Cross reference person_id with people.id
SELECT name, phone_number, passport_number, license_plate
FROM people
WHERE id IN (
    SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE year = 2021
        AND month = 07
        AND day = 28
        AND atm_location = "Leggett Street"
        AND transaction_type = "withdraw"));

-- This gives us 4 suspects who also left within 10 minutes of the crime: Iman, Luca, Diana, Bruce.
-- Let's check Raymond's tip that the thief made a call as they were leaving for less than a minute
SELECT id, caller, receiver, duration
FROM phone_calls
WHERE year = 2021
AND month = 07
AND day = 28
AND duration <= 60;

-- Let's cross reference the caller numbers with owner names
SELECT name, phone_number
FROM people
WHERE phone_number IN (
    SELECT caller
    FROM phone_calls
    WHERE year = 2021
    AND month = 07
    AND day = 28
    AND duration <= 60
);

-- This gives us 4 suspects from Ruth's tip: Sofia, Diana, Kelsey, Bruce and 5 suspects from Eugene's tip: Kenny, Benista, Taylor, Diana, Bruce, and 2 Suspect from Ruth's tip and Eugene's Tip: Diana, Bruce
-- Let's also check Raymond's tip that the thief was planning to take the earliest flight out of Fiftyville on 7/29/2021, and asked the accomplice to purchase the ticket