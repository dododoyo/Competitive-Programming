class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_maximum = max(candies);
        for i in range(len(candies)):
            candies[i] = (candies[i] + extraCandies) >= current_maximum;
        return candies;
            
        