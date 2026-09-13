-- Deliberately wrong: NULL is not compared with =.
SELECT operator_id FROM operators LEFT JOIN qualifications USING(operator_id) WHERE expires_on = NULL;
