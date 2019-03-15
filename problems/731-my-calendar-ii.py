class MyCalendarTwo:

    def __init__(self):
        self.double_booked = []
        self.single_booked = []

    def book(self, start, end):
        for i, j in self.double_booked:
            if start < j and end > i:
                return False
        for i, j in self.single_booked:
            if start < j and end > i:
                self.double_booked.append((max(start, i), min(end, j)))
        self.single_booked.append((start, end))
        return True
