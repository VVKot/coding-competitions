import datetime


class Solution:

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day_names = ["Monday", "Tuesday", "Wednesday",
                     "Thursday", "Friday", "Saturday", "Sunday"]
        date = datetime.datetime(year, month, day)
        return day_names[date.weekday()]
