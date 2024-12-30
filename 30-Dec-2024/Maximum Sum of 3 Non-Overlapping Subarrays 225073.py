# Problem: Maximum Sum of 3 Non-Overlapping Subarrays - https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) - k + 1

        sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            sums.append(sums[-1] - nums[i - k] + nums[i])

        memo = [[-1] * 4 for _ in range(n)]
        indices = []

        self._dp(sums, k, 0, 3, memo)
        self._dfs(sums, k, 0, 3, memo, indices)

        return indices

    def _dp(self, sums, k, idx, rem, memo):
        if rem == 0:
            return 0
        if idx >= len(sums):
            return float("-inf") if rem > 0 else 0

        if memo[idx][rem] != -1:
            return memo[idx][rem]

        take = sums[idx] + self._dp(sums, k, idx + k, rem - 1, memo)
        not_take = self._dp(sums, k, idx + 1, rem, memo)

        memo[idx][rem] = max(take, not_take)
        return memo[idx][rem]

    def _dfs(self, sums, k, idx, rem, memo, indices):
        if rem == 0 or idx >= len(sums):
            return

        take = sums[idx] + self._dp(sums, k, idx + k, rem - 1, memo)
        not_take = self._dp(sums, k, idx + 1, rem, memo)

        if take >= not_take: 
            indices.append(idx)
            self._dfs(sums, k, idx + k, rem - 1, memo, indices)
        else:
            self._dfs(sums, k, idx + 1, rem, memo, indices)