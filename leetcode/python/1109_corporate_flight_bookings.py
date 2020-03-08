from typing import List


class Solution:

    def corpFlightBookings(self,
                           bookings: List[List[int]], n: int) -> List[int]:
        booked_seats = [0] * n
        for start, end, seats_count in bookings:
            booked_seats[start-1] += seats_count
            if end < n:
                booked_seats[end] -= seats_count
        for i in range(1, n):
            booked_seats[i] += booked_seats[i-1]
        return booked_seats
