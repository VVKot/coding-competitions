import bisect


class MyCalendarThree:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> int:
        bisect.insort(self.bookings, (start, 1))
        bisect.insort(self.bookings, (end, -1))
        return self._get_max_bookings()

    def _get_max_bookings(self) -> int:
        max_bookings = bookings = 0
        for _, booking_diff in self.bookings:
            bookings += booking_diff
            max_bookings = max(max_bookings, bookings)
        return max_bookings
