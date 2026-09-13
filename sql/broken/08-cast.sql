-- Dangerous: SQLite silently casts 'ten' to 0. This is not validation.
SELECT SUM(CAST(minutes AS INTEGER)) FROM flight_intake;
