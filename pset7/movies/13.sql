--write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.

SELECT title FROM movies, stars, people
WHERE people.id = stars.person_id
AND stars.movie_id = movies.id
AND name = "Kevin Bacon";

SELECT * FROM stars WHERE movie_id IN ()