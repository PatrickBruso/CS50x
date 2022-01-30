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
WHERE name IN(
    SELECT name
      FROM people
     WHERE license_plate
        IN (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE year = 2021
            AND month = 07
            AND day = 28
            AND hour = 9  AND minute > 13 OR hour = 10 AND minute < 17
));
