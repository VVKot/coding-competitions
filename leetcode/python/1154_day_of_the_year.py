class Solution:

    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        day += sum(self.DAYS_IN_MONTH[:month-1])
        february_index = 2
        if self.is_leap(year) and month > february_index:
            day += 1
        return day

    def is_leap(self, year: int) -> bool:
        if not year % 400:
            return True
        if not year % 100:
            return False
        if not year % 4:
            return True
        return False
