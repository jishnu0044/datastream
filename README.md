# datastream

A micro-framework for capturing, buffering, and computing moving aggregates on high-frequency streaming data.

## Architecture
- `Buffer`: Fast, thread-safe memory storage for incoming data points.
- `Pipeline`: Orchestrates ingestion from sources and passes data to analytics engines.

## Setup
```bash
python run_pipeline.py
