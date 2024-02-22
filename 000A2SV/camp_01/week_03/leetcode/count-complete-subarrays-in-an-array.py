class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        return self.subarrayWithKDistinctElements(nums,k)
    def subarrayWithKDistinctElements(self,nums,k):
        solution, left, n = 0, 0, len(nums) 
        distincts = defaultdict(int)
        for right in range(n):
            distincts[nums[right]] += 1
            while len(distincts) == k:
                solution += n-right
                distincts[nums[left]] -= 1
                if distincts[nums[left]] == 0:
                    del distincts[nums[left]]
                left += 1
        return solution        