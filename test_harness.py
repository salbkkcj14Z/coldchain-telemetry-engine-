import time
import math
import random
import json
from datetime import datetime, timezone
from typing import List, Dict, Any

def percentile_linear(data: List[float], percentile: float, *, data_is_sorted: bool = False) -> float:
    """
    Returns the percentile using linear interpolation between rank points (inclusive).
    """
    if not 0.0 <= percentile <= 100.0:
        raise ValueError("percentile must be between 0 and 100")

    if not data:
        raise ValueError("data must not be empty")

    arr = data if data_is_sorted else sorted(data)
    n = len(arr)
    if n == 1:
        return float(arr[0])

    k = (n - 1) * (percentile / 100.0)
    f = int(math.floor(k))
    c = f + 1

    if c >= n:
        return float(arr[-1])

    return float(arr[f] * (c - k) + arr[c] * (k - f))


def generate_synthetic_payload(device_id: str) -> Dict[str, Any]:
    """Generates a combined physical and cognitive edge payload."""
    return {
        "device_id": device_id,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "telemetry": {
            "ambient_temp_c": round(random.uniform(18.0, 32.0), 2),
            "internal_temp_c": round(random.uniform(-22.0, -18.0), 2),
            "compressor_power_kw": round(random.uniform(2.1, 4.8), 2),
            "door_open": random.choice([True, False, False, False])
        },
        "cognitive_state": {
            "working_memory_hash": "a8f3b9c2d1e045f6a7b8c9d0e1f2a3b4",
            "adaptation_vector": [
                round(random.uniform(-1.0, 1.0), 4),
                round(random.uniform(-1.0, 1.0
