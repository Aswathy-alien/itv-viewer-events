
import apache_beam as beam

from events import create_event
from ingestion import ingest_event


def run_pipeline(number_of_events=20):
    """Generate, validate, and count simulated viewer events."""

    # Generate a finite batch of viewer events.
    sample_events = [
        create_event() for _ in range(number_of_events)
    ]

    with beam.Pipeline() as pipeline:
        (
            pipeline
            | "Create viewer events" >> beam.Create(sample_events)
            | "Validate events"
            >> beam.Map(ingest_event)
            | "Keep accepted events"
            >> beam.Filter(
                lambda result: result["status"] == "accepted"
            )
            | "Extract accepted event data"
            >> beam.Map(lambda result: result["event"])
            | "Build programme-event keys"
            >> beam.Map(
                lambda event: (
                    (event["programme_id"], event["event_type"]),
                    1,
                )
            )
            | "Count events by programme and type"
            >> beam.CombinePerKey(sum)
            | "Display counts" >> beam.Map(print)
        )


if __name__ == "__main__":
    run_pipeline()
