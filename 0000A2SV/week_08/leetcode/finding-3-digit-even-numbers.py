class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        hmap, res = defaultdict(int), []
        for num in digits:
            hmap[num] += 1
        
        for num in range(100, 999, 2):
            checker = defaultdict(int)
            for digit in str(num):
                checker[int(digit)] += 1
            
            if all(map(lambda x: x in hmap and checker[x] <= hmap[x], checker)):
                res.append(num)
        
        return res