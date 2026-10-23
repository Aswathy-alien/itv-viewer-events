
from datetime import datetime
from typing import Any

EVENT_TYPES = {"play", "pause", "watch-progress"}


def validate_event(event: dict[str, Any]) -> tuple[bool, str]:
    """Check whether a viewer event has the expected structure."""

    required_fields = {
        "event_id",
        "viewer_id",
        "programme_id",
        "event_type",
        "watch_seconds",
        "event_timestamp",
    }

    missing_fields = required_fields - event.keys()

    if missing_fields:
        return False, f"Missing fields: {sorted(missing_fields)}"

    if event["event_type"] not in EVENT_TYPES:
        return False, "Invalid event_type"

    if not isinstance(event["watch_seconds"], int):
        return False, "watch_seconds must be an integer"

    if event["watch_seconds"] < 0:
        return False, "watch_seconds cannot be negative"

    try:
        datetime.fromisoformat(
            event["event_timestamp"].replace("Z", "+00:00")
        )
    except (ValueError, AttributeError):
        return False, "Invalid event_timestamp"

    return True, "Event is valid"
