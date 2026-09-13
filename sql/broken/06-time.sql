-- Deliberately non-repeatable: the exercise has a fixed reference date.
SELECT operator_id FROM qualifications WHERE expires_on < date('now');
