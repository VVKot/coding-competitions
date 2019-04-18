from bisect import insort


class MyCalendarThree:

    def __init__(self):
        self.booked = []

    def book(self, start, end):
        insort(self.booked, (start, 1))
        insort(self.booked, (end, -1))
        result = 0
        cum_sum = 0
        for t, val in self.booked:
            cum_sum += val
            result = max(result, cum_sum)
        return result
