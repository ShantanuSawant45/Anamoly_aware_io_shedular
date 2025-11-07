import time
from workload import generate_anomaly_workload
from scan_scheduler import scan_scheduler
from anomaly_scheduler import anomaly_aware_scheduler
from simulation import run_simulation, print_results

if __name__ == "__main__":
    the_workload = generate_anomaly_workload()

    print("\n" + "=" * 50)
    print("🚀 RUN 1: Testing with NORMAL SCAN Scheduler")
    print("=" * 50)
    time.sleep(2)

    results_scan = run_simulation(scan_scheduler, the_workload)
    print_results(results_scan)

    print("\n" + "=" * 50)
    print("✨ RUN 2: Testing with ANOMALY-AWARE Scheduler")
    print("=" * 50)
    time.sleep(2)

    results_aware = run_simulation(anomaly_aware_scheduler, the_workload)
    print_results(results_aware)

    print("\n--- DEMO COMPLETE ---")
