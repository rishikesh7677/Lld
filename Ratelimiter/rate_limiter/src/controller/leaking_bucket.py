import threading
from datetime import datetime


class LeakingBucketALgorithm:
    current_queue_size = 0

    def __init__(self, queue_size_capacity: int, rate_to_empty_queue: int):
        self.queue_size_capacity = queue_size_capacity
        self.rate_to_empty_queue_per_sec = rate_to_empty_queue
        self.lock = threading.lock()
        self.last_time_empty_queue_time = datetime.now()

    def empty_queue(self):
        with self.lock:
            now = datetime.now()
            elpased_time = now - self.last_time_empty_queue_time
            request_to_remove = int(elpased_time.total_seconds() * self.rate_to_empty_queue_per_sec)
            self.current_queue_size = min(self.queue_size_capacity, self.current_queue_size - request_to_remove)
            self.last_time_empty_queue_time = now

    def process_request_add_into_queue(self):
        with self.lock:
            if self.current_queue_size + 1 > self.queue_size_capacity:
                return False
            self.current_queue_size += 1
