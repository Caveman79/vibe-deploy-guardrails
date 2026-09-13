PRAGMA foreign_keys = ON;
CREATE TABLE customers (customer_id TEXT PRIMARY KEY, name TEXT NOT NULL, max_wind_kts INTEGER NOT NULL CHECK(max_wind_kts > 0));
CREATE TABLE operators (operator_id TEXT PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE aircraft (aircraft_id TEXT PRIMARY KEY, model TEXT NOT NULL, status TEXT NOT NULL CHECK(status IN ('available','maintenance')));
CREATE TABLE qualifications (operator_id TEXT REFERENCES operators, qualification TEXT NOT NULL, expires_on TEXT NOT NULL, PRIMARY KEY(operator_id, qualification));
CREATE TABLE missions (mission_id TEXT PRIMARY KEY, customer_id TEXT NOT NULL REFERENCES customers, aircraft_id TEXT NOT NULL REFERENCES aircraft, operator_id TEXT NOT NULL REFERENCES operators, planned_at TEXT NOT NULL, status TEXT NOT NULL CHECK(status IN ('completed','planned','cancelled')));
CREATE TABLE flight_logs (flight_id TEXT PRIMARY KEY, mission_id TEXT NOT NULL REFERENCES missions, minutes INTEGER NOT NULL CHECK(minutes > 0), landed_at TEXT NOT NULL);
CREATE TABLE maintenance (maintenance_id TEXT PRIMARY KEY, aircraft_id TEXT NOT NULL REFERENCES aircraft, opened_on TEXT NOT NULL, closed_on TEXT, description TEXT NOT NULL);
CREATE TABLE risk_approvals (mission_id TEXT PRIMARY KEY REFERENCES missions, decision TEXT NOT NULL CHECK(decision IN ('approved','hold')), approver TEXT NOT NULL);
CREATE TABLE releases (version TEXT PRIMARY KEY, released_on TEXT NOT NULL, status TEXT NOT NULL);
CREATE TABLE deployments (deployment_id TEXT PRIMARY KEY, customer_id TEXT NOT NULL REFERENCES customers, version TEXT NOT NULL REFERENCES releases, environment TEXT NOT NULL, deployed_at TEXT NOT NULL);
CREATE TABLE incidents (incident_id TEXT PRIMARY KEY, deployment_id TEXT NOT NULL REFERENCES deployments, opened_at TEXT NOT NULL, severity TEXT NOT NULL, description TEXT NOT NULL);
-- Intake is deliberately imperfect. It is NOT the authoritative flight record.
CREATE TABLE flight_intake (row_id INTEGER PRIMARY KEY, flight_id TEXT, mission_id TEXT, minutes TEXT, landed_at TEXT);
