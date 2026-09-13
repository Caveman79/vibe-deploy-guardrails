from contextlib import closing
"""Run one read-only SQLite query from a file; results print as a table."""
import argparse
from pathlib import Path
import sqlite3
from ops_data.seed import DEFAULT_DB


def connect(path=DEFAULT_DB):
    uri = Path(path).resolve().as_uri() + "?mode=ro"
    db = sqlite3.connect(uri, uri=True)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA query_only=ON")
    return db


def run(sql, path=DEFAULT_DB):
    with closing(connect(path)) as db:
        # Reject writes, ATTACH, schema mutations and PRAGMA changes as well as
        # opening the primary database read-only. This is a local learning tool.
        allowed = {sqlite3.SQLITE_SELECT, sqlite3.SQLITE_READ, sqlite3.SQLITE_FUNCTION, sqlite3.SQLITE_RECURSIVE}
        db.set_authorizer(lambda action, *_: sqlite3.SQLITE_OK if action in allowed else sqlite3.SQLITE_DENY)
        cursor = db.execute(sql)
        return [column[0] for column in cursor.description], [tuple(row) for row in cursor.fetchall()]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    args = parser.parse_args()
    try:
        names, rows = run(args.file.read_text(), args.db)
        print(" | ".join(names))
        for row in rows:
            print(" | ".join("NULL" if value is None else str(value) for value in row))
        print(f"{len(rows)} row(s)")
    except (OSError, sqlite3.Error) as error:
        parser.exit(1, f"Query failed: {error}\nCreate the database first with python3 -m ops_data.seed.\n")
