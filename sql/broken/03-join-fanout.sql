-- Deliberately wrong: qualifications are joined without matching operators.
SELECT SUM(f.minutes) AS total_minutes FROM flight_logs f JOIN qualifications q ON 1=1;
