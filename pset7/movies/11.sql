--write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.

SELECT title FROM movies WHERE id IN (SELECT movie_id FROM stars WHERE person_id IN (SELECT id FROM people WHERE name = "Chadwick Boseman")) ORDER BY (SELECT rating FROM ratings) DESC LIMIT 5;

-- need to use join?