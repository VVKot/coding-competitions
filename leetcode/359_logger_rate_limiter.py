class Logger:

    PRINT_INTERVAL = 10

    def __init__(self):
        self.buckets = [-1 for _ in range(self.PRINT_INTERVAL)]
        self.sets = [set() for _ in range(self.PRINT_INTERVAL)]

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        bucket_index = timestamp % self.PRINT_INTERVAL
        if self.buckets[bucket_index] != timestamp:
            self.sets[bucket_index].clear()
            self.buckets[bucket_index] = timestamp
        for i, bucket_timestamp in enumerate(self.buckets):
            if timestamp - bucket_timestamp < self.PRINT_INTERVAL:
                if message in self.sets[i]:
                    return False
        self.sets[bucket_index].add(message)
        return True
