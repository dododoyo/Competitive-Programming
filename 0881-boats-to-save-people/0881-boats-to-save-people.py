class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p1 = 0
        p2 = len(people) -1
        boats = 0
        people.sort()
        
        while(not(p1>p2)):
            if(people[p1]+people[p2] > limit):
                p2 -= 1
            else:
                p1 += 1
                p2 -= 1
            boats += 1
        return boats
                
                
        