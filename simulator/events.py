
import json
import random
import time
import uuid
from datetime import datetime, timezone

EVENT_TYPES = ["play", "pause", "watch-progress"]
PROGRAMMES = ["drama_001", "documentary_002", "comedy_003"]


def create_event():
    """Create one simulated viewer activity event."""
    event_type = random.choice(EVENT_TYPES)

    return {
        "event_id": str(uuid.uuid4()),
        "viewer_id": f"viewer_{random.randint(1, 10):03d}",
        "programme_id": random.choice(PROGRAMMES),
        "event_type": event_type,
        "watch_seconds": (
            random.randint(1, 60)
            if event_type == "watch-progress"
            else 0
        ),
        "event_timestamp": datetime.now(timezone.utc).isoformat(),
    }


def main():
    print("Starting viewer event simulator. Press Ctrl+C to stop.")

    try:
        while True:
            event = create_event()
            print(json.dumps(event))
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nSimulator stopped.")


if __name__ == "__main__":
    main()
