class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right,boats = 0,len(people)-1,0
        while right >= left:
            if people[left]+people[right] <= limit or left == right:
                right,left = right-1,left+1
            else:
                right= right-1
            boats += 1
        return boats
        