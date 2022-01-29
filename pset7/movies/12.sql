--write a SQL query to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.

SELECT title FROM movies, stars, people
 WHERE people.id = stars.person_id
   AND stars.movie_id = movies.id
   AND name = "Johnny Depp"
   AND title IN (
       SELECT title FROM movies, stars, people
        WHERE people.id = stars.person_id
          AND stars.movie_id = movies.id
          AND name = "Helena Bonham Carter"
       );