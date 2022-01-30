-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Check the crime scene reports table for the date of July 28, 2021 and Humphrey Street
SELECT description, id
  FROM crime_scene_reports
 WHERE year = 2021
   AND month = 07
   AND day = 28
   AND street = "Humphrey Street";

   -- Obtained crime scene id of 295.  Let's check bakery logs.
SELECT id, activity
  FROM bakery_security_logs
 WHERE year = 2021
   AND month = 07
   AND day = 28
   AND hour = 10
   AND minute = 15;