class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        reserved_seats = [0]*(n+1)
        for booking in bookings:
            first,last,seat = booking[0],booking[1],booking[2]
            reserved_seats[first-1] += seat
            reserved_seats[last] -= seat
        for i in range(1,n):
            reserved_seats[i] += reserved_seats[i-1]
        return reserved_seats[:-1]
        
