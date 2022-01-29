--write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.


SELECT title FROM movies WHERE id IN ()
SELECT id IN people WHERE name = "Chadwick Boseman"

ORDER BY rating DESC LIMIT 5;