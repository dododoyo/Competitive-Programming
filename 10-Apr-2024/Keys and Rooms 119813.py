# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0]

        while stack:
            room = stack.pop()
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)

        return len(visited) == len(rooms)