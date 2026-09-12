import itertools
import json
import threading
import unittest
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import urlopen
from guardrails.app import CHECKS, Config, handler_for, in_cohort, is_ready


class LogicTests(unittest.TestCase):
    def test_every_release_check_is_required(self):
        for flags in itertools.product((True, False), repeat=3):
            with self.subTest(flags=flags):
                self.assertEqual(is_ready(dict(zip(CHECKS, flags))), all(flags))

    def test_missing_or_truthy_evidence_is_not_approval(self):
        for value in ({}, {"review": True, "tests": True},
                      {"review": "true", "tests": True, "rollback": True}):
            self.assertFalse(is_ready(value))

    def test_config_defaults_and_valid_environments(self):
        self.assertEqual(Config.from_env({}), Config())
        for name in ("dev", "test", "staging", "prod"):
            self.assertEqual(Config.from_env({"APP_ENV": name}).environment, name)
        self.assertEqual(Config.from_env({"ROLLOUT_PERCENT": "100"}).rollout_percent, 100)

    def test_config_rejects_bad_values(self):
        for env in ({"APP_ENV": "production"}, {"APP_VERSION": "bad\nvalue"},
                    {"ROLLOUT_PERCENT": "-1"}, {"ROLLOUT_PERCENT": "101"},
                    {"ROLLOUT_PERCENT": "true"}, {"ROLLOUT_PERCENT": "1.5"}):
            with self.subTest(env=env), self.assertRaises(ValueError):
                Config.from_env(env)

    def test_flag_boundaries_stability_and_monotonicity(self):
        for cohort in ("alpha", "bravo", "charlie", "training-team"):
            self.assertFalse(in_cohort(cohort, 0))
            self.assertTrue(in_cohort(cohort, 100))
            values = [in_cohort(cohort, p) for p in range(101)]
            self.assertEqual(values, sorted(values))
        self.assertEqual(in_cohort("alpha", 50), in_cohort("alpha", 50))


class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), handler_for(Config("test", "test-build", 100)))
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def get(self, path):
        try:
            response = urlopen(self.base + path, timeout=3)
        except HTTPError as error:
            response = error
        with response:
            return response.status, response.headers, response.read()

    def test_homepage_and_health(self):
        self.assertIn(b"controlled change", self.get("/")[2])
        status, headers, body = self.get("/healthz")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body), {"status": "ok", "environment": "test", "version": "test-build"})
        self.assertEqual(headers["Cache-Control"], "no-store")
        self.assertEqual(len(headers["X-Request-ID"]), 32)

    def test_readiness_and_flag(self):
        status, _, body = self.get("/api/readiness?review=true&tests=true&rollback=true")
        self.assertEqual(status, 200)
        self.assertTrue(json.loads(body)["ready"])
        self.assertIn("guidance", json.loads(body))
        self.assertFalse(json.loads(self.get("/api/readiness")[2])["ready"])

    def test_invalid_requests(self):
        for query in ("review=yes", "review=true&review=false", "cohort=", "secret=demo",
                      "review=true&tests=true&rollback=true&cohort=a&extra=b", "cohort="+"a"*1025):
            with self.subTest(query=query):
                self.assertEqual(self.get("/api/readiness?"+query)[0], 400)
        self.assertEqual(self.get("/.env")[0], 404)

    def test_logs_exclude_query_and_unknown_path(self):
        with self.assertLogs("guardrails", level="INFO") as logs:
            self.get("/private-demo-secret?token=demo-secret")
        self.assertNotIn("demo-secret", "".join(logs.output))
        self.assertIn('"route": "unknown"', "".join(logs.output))

    def test_request_ids_are_unique(self):
        self.assertNotEqual(self.get("/healthz")[1]["X-Request-ID"], self.get("/healthz")[1]["X-Request-ID"])


if __name__ == "__main__":
    unittest.main()
