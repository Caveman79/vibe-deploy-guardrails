from contextlib import closing
"""Read-only synthetic mission endpoints; filtering is not authorization."""
import hmac
import os
from urllib.parse import parse_qs
from ops_data.query import connect


def response(path, query_string, authorization, db_path):
    if len(query_string) > 256:
        return 400, {"error": "invalid query"}
    try:
        query = parse_qs(query_string, keep_blank_values=True, max_num_fields=2)
    except ValueError:
        return 400, {"error": "invalid query"}
    if set(query) - {"customer", "offset"} or any(len(value) != 1 for value in query.values()):
        return 400, {"error": "invalid query"}
    customer = query.get("customer", [None])[0]
    offset = query.get("offset", ["0"])[0]
    if customer not in {None, "C01", "C02"} or not offset.isascii() or not offset.isdigit() or len(offset) > 4:
        return 400, {"error": "invalid query"}
    if path == "/api/customer-config":
        token = os.environ.get("DEMO_API_TOKEN", "")
        if len(token) < 16:
            return 503, {"error": "demo authentication is not configured"}
        if not hmac.compare_digest(authorization.encode(), ("Bearer " + token).encode()):
            return 401, {"error": "authentication required"}
        if customer is None or "offset" in query:
            return 400, {"error": "choose one customer"}
    with closing(connect(db_path)) as db:
        if path == "/api/missions":
            rows = db.execute("SELECT mission_id,customer_id,aircraft_id,operator_id,planned_at,status FROM missions WHERE (? IS NULL OR customer_id=?) ORDER BY mission_id LIMIT 4 OFFSET ?", (customer, customer, int(offset))).fetchall()
            return 200, {"items": [dict(x) for x in rows[:3]], "next_offset": int(offset)+3 if len(rows)>3 else None}
        if path == "/api/customer-config":
            return 200, dict(db.execute("SELECT customer_id,max_wind_kts FROM customers WHERE customer_id=?",(customer,)).fetchone())
        if query:
            return 400, {"error": "summary takes no query parameters"}
        return 200, {"missions": db.execute("SELECT COUNT(*) FROM missions").fetchone()[0], "planned": db.execute("SELECT COUNT(*) FROM missions WHERE status='planned'").fetchone()[0], "flight_minutes": db.execute("SELECT SUM(minutes) FROM flight_logs").fetchone()[0], "synthetic": True}
