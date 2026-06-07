import time
from datastream import StreamPipeline

def run_simulation():
    print("[Ingestion] Starting DataStream Engine...")
    pipeline = StreamPipeline(metric_name="CPU_Utilization_Index")

    # --- Scenario 1: Normal Operation (Multiple Points) ---
    print("\n[Ingestion] Feeding Batch 1 (Multiple data points)...")
    pipeline.ingest(45.2)
    pipeline.ingest(48.7)
    pipeline.ingest(46.1)
    
    metrics_1 = pipeline.process_batch()
    print(f"[Analytics Output]: {metrics_1}")

    # --- Scenario 2: Bug Triggering Event (Exactly 1 Point) ---
    print("\n[Ingestion] Feeding Batch 2 (Edge Case: Exactly 1 point)...")
    pipeline.ingest(50.0)
    
    metrics_2 = pipeline.process_batch()
    print(f"[Analytics Output]: {metrics_2}")

if __name__ == "__main__":
    run_simulation()