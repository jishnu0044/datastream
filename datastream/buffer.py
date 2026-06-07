import threading
from typing import List, Tuple

class MetricBuffer:
    """Thread-safe storage for streaming raw metric data."""
    def __init__(self, max_size: int = 1000):
        self.max_size = max_size
        self.storage: List[Tuple[float, float]] = [] # Stores (timestamp, value)
        self.lock = threading.Lock()

    def append(self, timestamp: float, value: float) -> None:
        with self.lock:
            if len(self.storage) < self.max_size:
                self.storage.append((timestamp, value))

    def flush_all(self) -> List[Tuple[float, float]]:
        with self.lock:
            data = self.storage.copy()
            self.storage.clear()
            return data