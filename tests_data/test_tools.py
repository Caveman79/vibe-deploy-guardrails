from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock
import requests
from ops_data.analyze import analyze
from ops_data.client import fetch_missions

class ToolTests(unittest.TestCase):
    def test_intake_quarantines_bad_rows(self):
        report,rejected=analyze('fixtures/flight_intake.csv','fixtures/missions.json')
        self.assertEqual((report['accepted_rows'],report['rejected_rows'],report['total_minutes']),(4,5,135))
        self.assertIn('unknown_mission',';'.join(rejected.reasons))

    def test_conflicting_duplicates_quarantine_both(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'input.csv'
            p.write_text('flight_id,mission_id,minutes,landed_at\nF1,M01,10,2026-09-01T00:00:00Z\nF1,M01,20,2026-09-01T00:00:00Z\n')
            report,_=analyze(p,'fixtures/missions.json')
            self.assertEqual(report['accepted_rows'],0)

    def test_client_rejects_stuck_pagination_and_redirect(self):
        session=Mock(); reply=session.get.return_value
        reply.status_code=200; reply.json.return_value={'items':[],'next_offset':0}
        with self.assertRaises(ValueError): fetch_missions('http://127.0.0.1:8000',session=session)
        reply.status_code=302
        with self.assertRaises(ValueError): fetch_missions('http://127.0.0.1:8000',session=session)

    def test_client_does_not_hide_timeout(self):
        session=Mock();session.get.side_effect=requests.Timeout()
        with self.assertRaises(requests.Timeout):fetch_missions('http://127.0.0.1:8000',session=session)
