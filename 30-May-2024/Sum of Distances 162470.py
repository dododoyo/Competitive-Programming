# Problem: Sum of Distances - https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        """
        Though our implementation might look like 
        O(n^2) in both best and worst cases it is O(n)"""
        
        index_map, solution = defaultdict(list), [0]*len(nums)
        for i in range(len(nums)):
            index_map[nums[i]].append(i)

        for number,index_list in index_map.items():
            m = len(index_list)
            if m > 1:
                index_distances = self.findDistance(index_list)
                for i in range(m):
                    solution[index_list[i]] = index_distances[i]
        return solution
    def findDistance(self,nums):
        n = len(nums)
        solution = [0]*n

        prefix_sum, suffix_sum, solution = [nums[0]]*n,[nums[-1]]*n,[0]*n
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
            suffix_sum[n-i-1] = suffix_sum[n-i] + nums[n-i-1]
        for i in range(n):
            if i == 0:
                solution[i] += suffix_sum[i+1] - (n-1)*nums[i]
            elif i == n-1:
                solution[i] += nums[i]*(n-1) - prefix_sum[i-1]
            else:
                solution[i] += nums[i]*(2*i -n + 1) + suffix_sum[i+1] - prefix_sum[i-1]
        return solution
