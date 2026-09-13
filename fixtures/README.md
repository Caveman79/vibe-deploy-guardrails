# Fictional training data

All organizations, people, missions and records here are synthetic. This is not an
aviation decision system. Dates are fixed in September 2026; use **2026-09-15** as
the assessment date, never the computer's current date.

`flight_intake.csv` has nine raw rows and intentional defects. The seed script loads
it into `flight_intake`, separate from the authoritative four-row `flight_logs` table.
A duplicate is not an extra flight. A missing duration is not zero. Preserve and
quarantine questionable rows rather than silently changing operational history.

`missions.json` is a small valid-ID lookup for Python exercises. `customer-config.json`
is public, non-secret demonstration configuration. Customer limits are invented
requirements for this exercise, not regulatory or manufacturer limits.
