class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        request_list = [0]*(len(nums)+1)
        for request in requests:
            start,end = request
            request_list[start] += 1
            request_list[end+1] -= 1
        for i in range(1,len(nums)+1):
            request_list[i] += request_list[i-1]
        request_list.sort(reverse=True)
        nums.sort(reverse=True)
        solution = 0
        for i in range(len(nums)):
            solution += nums[i]*request_list[i]
        return solution%MOD
    