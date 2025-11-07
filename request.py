class Request:
    """A simple class to represent an I/O request."""

    def __init__(self, arrival_time, process_id, block_number):
        self.arrival_time = arrival_time
        self.process_id = process_id
        self.block_number = block_number
        self.completion_time = 0
        self.wait_time = 0

    def __repr__(self):
        return f"[t={self.arrival_time}, PID={self.process_id}, Block={self.block_number}]"
