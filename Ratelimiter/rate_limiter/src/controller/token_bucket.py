from datetime import datetime
import threading


class TokenBucketAlgorith:
    used_token_count = 0

    def __init__(self, bucket_size: int, refil_rate_per_min: int) -> None:
        self.bucket_size = bucket_size
        self.refil_rate_per_min = refil_rate_per_min
        self.current_token = 0
        self.last_time_filled = datetime.now()
        self.Thread_lock = threading.Lock()

    def add_token(self):

        with self.Thread_lock:
            now = datetime.now()
            elapsed_time = now - self.last_update
            tokens_to_add = elapsed_time * self.refil_rate_per_min
            self.current_token = min(self.bucket_size, self.current_token + tokens_to_add)
            self.last_time_filled = now

    def consume_token(self):

        with self.Thread_lock:
            if self.current_token > 0:
                self.current_token -= 1
                self.used_token_count = self.bucket_size - self.current_token
                return True

        return False
