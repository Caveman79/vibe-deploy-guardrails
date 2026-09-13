"""Create a deterministic synthetic SQLite database; never overwrite an existing file."""
import argparse
import csv
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "data" / "operations.db"


def seed(path=DEFAULT_DB):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"{path} already exists; keep it or choose --db with a new filename")
    # Exclusive creation avoids overwriting a learner's work even under a race.
    path.touch(exist_ok=False)
    try:
        with sqlite3.connect(path) as db:
            db.executescript((Path(__file__).with_name("schema.sql")).read_text())
            db.executemany("INSERT INTO customers VALUES (?,?,?)", [("C01","Harbor Survey",20),("C02","Ridge Utilities",15)])
            db.executemany("INSERT INTO operators VALUES (?,?)", [("O01","Alex River"),("O02","Sam Vale"),("O03","Taylor Reed"),("O04","Morgan Lake")])
            db.executemany("INSERT INTO aircraft VALUES (?,?,?)", [("A01","Scout","available"),("A02","Scout","maintenance"),("A03","Mapper","available")])
            db.executemany("INSERT INTO qualifications VALUES (?,?,?)", [("O01","mission_operator","2027-01-01"),("O02","mission_operator","2026-08-31"),("O03","mission_operator","2026-12-31")])
            missions = [
                ("M01","C01","A01","O01","2026-09-01T09:00:00Z","completed"),
                ("M02","C01","A01","O01","2026-09-02T09:00:00Z","completed"),
                ("M03","C02","A03","O03","2026-09-02T10:00:00Z","completed"),
                ("M04","C02","A03","O03","2026-09-03T10:00:00Z","completed"),
                ("M05","C01","A02","O02","2026-09-15T09:00:00Z","planned"),
                ("M06","C02","A03","O04","2026-09-15T10:00:00Z","planned"),
                ("M07","C01","A01","O01","2026-09-16T09:00:00Z","planned"),
                ("M08","C02","A03","O03","2026-09-04T10:00:00Z","cancelled")]
            db.executemany("INSERT INTO missions VALUES (?,?,?,?,?,?)", missions)
            db.executemany("INSERT INTO flight_logs VALUES (?,?,?,?)",[("F01","M01",30,"2026-09-01T09:30:00Z"),("F02","M02",45,"2026-09-02T09:45:00Z"),("F03","M03",20,"2026-09-02T10:20:00Z"),("F04","M04",40,"2026-09-03T10:40:00Z")])
            db.execute("INSERT INTO maintenance VALUES ('MX01','A02','2026-09-10',NULL,'Battery inspection outstanding')")
            db.executemany("INSERT INTO risk_approvals VALUES (?,?,?)",[("M05","hold","Synthetic reviewer"),("M07","approved","Synthetic reviewer")])
            db.executemany("INSERT INTO releases VALUES (?,?,?)",[("r1","2026-09-01","known-good"),("r2","2026-09-10","candidate")])
            db.executemany("INSERT INTO deployments VALUES (?,?,?,?,?)",[("D01","C01","r1","prod","2026-09-01T08:00:00Z"),("D02","C01","r2","staging","2026-09-10T08:00:00Z"),("D03","C02","r1","prod","2026-09-01T08:00:00Z")])
            db.execute("INSERT INTO incidents VALUES ('I01','D02','2026-09-10T09:00:00Z','medium','Staging summary omitted a missing qualification')")
            with (ROOT / "fixtures" / "flight_intake.csv").open(newline="") as source:
                rows = csv.DictReader(source)
                db.executemany("INSERT INTO flight_intake(flight_id,mission_id,minutes,landed_at) VALUES (?,?,?,?)",[(x['flight_id'] or None,x['mission_id'] or None,x['minutes'] or None,x['landed_at'] or None) for x in rows])
    except Exception:
        path.unlink(missing_ok=True)
        raise
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    args = parser.parse_args()
    try:
        print(f"Created synthetic training database: {seed(args.db)}")
    except FileExistsError as error:
        parser.exit(1, f"{error}\n")
