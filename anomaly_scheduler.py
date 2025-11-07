from scan_scheduler import scan_scheduler

def anomaly_aware_scheduler(queue, head_position, state):
    """Smart scheduler that wraps SCAN and adds anomaly detection."""

    is_anomaly = False
    anomaly_pid = None

    if len(queue) > 10:
        pid_counts = {}
        for req in queue:
            pid_counts[req.process_id] = pid_counts.get(req.process_id, 0) + 1

        total_reqs = len(queue)
        for pid, count in pid_counts.items():
            if (count / total_reqs) > 0.70:
                is_anomaly = True
                anomaly_pid = pid
                break

    current_direction = state.get('scan_direction', 1)

    if is_anomaly:
        print(f"    (!) Anomaly Detected! 'Noisy App' ({anomaly_pid}) is flooding the queue.")

        fair_request = next((req for req in queue if req.process_id != anomaly_pid), None)
        if fair_request:
            print(f"    (!) Prioritizing 'App 1' to prevent starvation.")
            return fair_request, current_direction
        else:
            print(f"    (!) Only 'Noisy App' requests left. Running SCAN.")
            next_req, new_dir = scan_scheduler(queue, head_position, current_direction)
            state['scan_direction'] = new_dir
            return next_req, new_dir
    else:
        print("    (N) Normal Mode. Running SCAN.")
        next_req, new_dir = scan_scheduler(queue, head_position, current_direction)
        state['scan_direction'] = new_dir
        return next_req, new_dir
