--write a SQL query to list the names of all people who starred in Toy Story.

SELECT name FROM people WHERE id = (SELECT name FROM movies WHERE name = "Toy Story");