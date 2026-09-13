import os
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch
from guardrails import course
from ops_data.seed import seed
from ops_data.query import run
from ops_data.api import response

class CourseDataTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.db=seed(Path(self.temp.name)/'ops.db')

    def test_preserves_existing_database(self):
        original=self.db.read_bytes()
        with self.assertRaises(FileExistsError): seed(self.db)
        self.assertEqual(original,self.db.read_bytes())

    def test_query_totals_and_write_rejection(self):
        self.assertEqual(run('SELECT SUM(minutes) FROM flight_logs',self.db)[1],[(135,)])
        for sql in ('DELETE FROM missions',"ATTACH DATABASE ':memory:' AS extra",'PRAGMA query_only=OFF'):
            with self.assertRaises(sqlite3.Error): run(sql,self.db)

    def test_reference_queries_execute(self):
        for path in Path('sql/solutions').glob('*.sql'):
            with self.subTest(path=path): self.assertTrue(run(path.read_text(),self.db)[1])

    def test_complete_pagination_and_invalid_inputs(self):
        items=[]; offset=0
        while True:
            status,data=response('/api/missions',f'offset={offset}','',self.db)
            self.assertEqual(status,200);items.extend(data['items'])
            offset=data['next_offset']
            if offset is None: break
        self.assertEqual(len(items),8)
        self.assertEqual(len({x['mission_id'] for x in items}),8)
        for query in ('customer=unknown','offset=-1','customer=C01&customer=C02'):
            self.assertEqual(response('/api/missions',query,'',self.db)[0],400)

    def test_config_authentication(self):
        with patch.dict(os.environ,{},clear=True):
            self.assertEqual(response('/api/customer-config','customer=C01','',self.db)[0],503)
        with patch.dict(os.environ,{'DEMO_API_TOKEN':'synthetic-token-for-testing'}):
            self.assertEqual(response('/api/customer-config','customer=C01','',self.db)[0],401)
            code,data=response('/api/customer-config','customer=C01','Bearer synthetic-token-for-testing',self.db)
            self.assertEqual((code,data['max_wind_kts']),(200,20))

    def test_all_registered_lessons_render_and_no_file_traversal(self):
        for name in course.FILES:
            with self.subTest(name=name): self.assertIn(b'<h1>',course.lesson(name))
        for name in ('../../etc/passwd','.env.demo','guardrails/app.py'):
            with self.assertRaises(ValueError): course.lesson(name)
        self.assertNotIn('<script>',course.inline('<script>alert(1)</script>',Path('START_HERE.md')))
