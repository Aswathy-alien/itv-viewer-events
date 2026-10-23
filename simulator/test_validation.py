
import unittest

from validation import validate_event


class TestValidateEvent(unittest.TestCase):
    def setUp(self):
        self.event = {
            "event_id": "event-001",
            "viewer_id": "viewer_001",
            "programme_id": "drama_001",
            "event_type": "play",
            "watch_seconds": 0,
            "event_timestamp": "2026-10-23T12:00:00+00:00",
        }

    def test_valid_event(self):
        valid, message = validate_event(self.event)
        self.assertTrue(valid, message)

    def test_invalid_event_type(self):
        self.event["event_type"] = "unknown"
        valid, _ = validate_event(self.event)
        self.assertFalse(valid)

    def test_negative_watch_seconds(self):
        self.event["watch_seconds"] = -5
        valid, _ = validate_event(self.event)
        self.assertFalse(valid)

    def test_missing_field(self):
        del self.event["viewer_id"]
        valid, _ = validate_event(self.event)
        self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main()
