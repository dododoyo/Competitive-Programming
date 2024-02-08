class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers_list = [0]*1005
        for trip in trips:
            passengers,frm,to = trip[0],trip[1],trip[2]
            passengers_list[frm] += passengers
            passengers_list[to] -= passengers
        maximum_passengers = passengers_list[0]
        for i in range(1,1005):
            passengers_list[i] += passengers_list[i-1]
            maximum_passengers = max(maximum_passengers,passengers_list[i])    
        return False if capacity < maximum_passengers else True


        