import random
from request import Request

def generate_anomaly_workload():
    """Generates a list of Request objects for the simulation."""
    workload = []

    for t in range(20):
        workload.append(Request(arrival_time=t * 5, process_id='App 1', block_number=random.randint(800, 1000)))

    print("--- ANOMALY INJECTED at t=100 ---")
    for _ in range(50):
        workload.append(Request(arrival_time=100, process_id='Noisy App', block_number=random.randint(100, 200)))

    for t in range(21, 30):
        workload.append(Request(arrival_time=t * 5 + 1, process_id='App 1', block_number=random.randint(800, 900)))

    workload.sort(key=lambda r: r.arrival_time)
    return workload
