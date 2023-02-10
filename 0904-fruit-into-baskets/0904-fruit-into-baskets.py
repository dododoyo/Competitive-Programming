from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int) # defaultdict to store the frequency of the elements in the subarray
        i, j = 0, 0 # variables i and j are used to keep track of the subarray boundaries
        for j in range(len(fruits)):
            count[fruits[j]] += 1 # increase the count of the current fruit
            if len(count) > 2: 
                count[fruits[i]] -= 1 # reduce the count of the first fruit
                if count[fruits[i]] == 0:
                    del count[fruits[i]] # remove the first fruit from the defaultdict if its count becomes 0
                i += 1 # move the start of the subarray to the right
        return j - i + 1 # return the length of the longest subarray with at most two unique elements