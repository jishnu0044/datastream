import threading
import time
from typing import Dict, Any
from .buffer import MetricBuffer
from .analytics import WindowAggregator

class StreamPipeline:
    def __init__(self, metric_name: str):
        self.metric_name = metric_name
        self.buffer = MetricBuffer()
        self.aggregator = WindowAggregator()
        self.is_active = False

    def ingest(self, value: float) -> None:
        """Ingests a single metric point into the underlying buffer."""
        current_time = time.time()
        self.buffer.append(current_time, value)

    def process_batch(self) -> Dict[str, Any]:
        """Flushes the buffer and computes descriptive metrics."""
        raw_data = self.buffer.flush_all()
        
        try:
            var_result = self.aggregator.calculate_variance(raw_data)
            return {
                "metric": self.metric_name,
                "count": len(raw_data),
                "variance": var_result,
                "status": "SUCCESS"
            }
        except Exception as e:
            return {"metric": self.metric_name, "status": f"ERROR: {str(e)}"}