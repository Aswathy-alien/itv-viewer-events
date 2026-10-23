
import json
import time

from events import create_event
from validation import validate_event


def ingest_event(event: dict) -> dict:
    """Validate an event before accepting it for processing."""

    valid, message = validate_event(event)

    if not valid:
        return {
            "status": "rejected",
            "reason": message,
        }

    return {
        "status": "accepted",
        "event": event,
    }


def main():
    print("Starting local ingestion. Press Ctrl+C to stop.")

    try:
        while True:
            event = create_event()
            result = ingest_event(event)
            print(json.dumps(result))
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nIngestion stopped.")


if __name__ == "__main__":
    main()
