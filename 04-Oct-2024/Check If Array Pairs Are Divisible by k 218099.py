# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 == 1: return False
        prev = collections.defaultdict(int)
        count = 0
        for i, num in enumerate(arr):
            key = k - (num % k)
            if key in prev and prev[key] >= 1:
                count += 1
                prev[key] -= 1
            else:
                prev[(num % k) or k] += 1
        return count == len(arr)//2