# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        newTimes = [0]*n
        for i in range(n):
            h,m = map(int,timePoints[i].split(":"))
            newTimes[i] = h*60 + m
        minTime  = float("inf")
        newTimes.sort()
        for i in range(1,n):
            minTime = min(minTime,newTimes[i] - newTimes[i-1])
        if newTimes[-1] > 12*60:
            minTime = min(minTime,newTimes[0] + (24*60-newTimes[-1]))
        # print(newTimes)
        return minTime