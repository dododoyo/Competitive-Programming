# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        m = len(meetings)
        que,available = [],[]
        rooms = [0]*n
        meetings.sort()
        duration = [b-a for a,b in meetings]

        for i in range(n):
            heappush(available , i)

        for meet in meetings:
            start , end = meet
            while len(que) and que[0][0] <= start:
                cavailable , curr_room = heappop(que)
                heappush(available , curr_room)

            if len(available):
                rooms[available[0]] += 1
                curr_room = heappop(available)
                heappush(que , (end , curr_room))
            else:
                rooms[que[0][1]] += 1
                time , curr_room = heappop(que)
                heappush(que , (time + end - start , curr_room))
        max_rooms = max(rooms)

        for index,room in enumerate(rooms):
            if room == max_rooms:
                return index