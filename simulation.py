def run_simulation(scheduler_function, workload):
    """Runs the simulation."""
    future_requests = list(workload)
    request_queue = []
    completed_requests = []

    current_time = 0
    head_position = 500
    scheduler_state = {'scan_direction': 1}

    while future_requests or request_queue:
        while future_requests and future_requests[0].arrival_time <= current_time:
            new_req = future_requests.pop(0)
            print(f"t={current_time}: Arrived {new_req}")
            request_queue.append(new_req)

        if request_queue:
            if scheduler_function.__name__ == "scan_scheduler":
                next_req, new_dir = scheduler_function(request_queue, head_position, scheduler_state['scan_direction'])
                scheduler_state['scan_direction'] = new_dir
            else:
                next_req, new_dir = scheduler_function(request_queue, head_position, scheduler_state)
                scheduler_state['scan_direction'] = new_dir

            if next_req:
                request_queue.remove(next_req)
                distance = abs(next_req.block_number - head_position)
                time_taken = max(1, int(distance / 10))
                current_time += time_taken
                head_position = next_req.block_number
                next_req.completion_time = current_time
                next_req.wait_time = current_time - next_req.arrival_time
                completed_requests.append(next_req)
                print(f"t={current_time}: Serviced {next_req} (Wait: {next_req.wait_time}t)")
            else:
                current_time += 1
        else:
            current_time += 1

    return completed_requests


def print_results(results):
    """Prints average wait time per process."""
    print("\n--- 📊 Final Results ---")
    stats = {}
    for req in results:
        pid = req.process_id
        stats.setdefault(pid, []).append(req.wait_time)

    for pid, times in stats.items():
        avg_wait = sum(times) / len(times)
        print(f"  Process ID: {pid}")
        print(f"    Total Requests: {len(times)}")
        print(f"    Average Wait Time: {avg_wait:.2f} ticks")
