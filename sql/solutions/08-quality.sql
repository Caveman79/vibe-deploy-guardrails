SELECT flight_id, COUNT(*) AS copies FROM flight_intake GROUP BY flight_id HAVING COUNT(*) > 1;
