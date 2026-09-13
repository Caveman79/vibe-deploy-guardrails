SELECT m.customer_id, COUNT(f.flight_id) AS flights, SUM(f.minutes) AS total_minutes FROM missions m JOIN flight_logs f ON f.mission_id=m.mission_id GROUP BY m.customer_id ORDER BY m.customer_id;
