import collections


class Logger:

    PRINT_INTERVAL = 10

    def __init__(self):
        self.can_print_on = collections.defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        allowed_timestamp = self.can_print_on[message]
        if timestamp < allowed_timestamp:
            return False
        self.can_print_on[message] = timestamp + self.PRINT_INTERVAL
        return True
