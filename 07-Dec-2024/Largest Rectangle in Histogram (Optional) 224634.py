# Problem: Largest Rectangle in Histogram (Optional) - https://leetcode.com/problems/largest-rectangle-in-histogram/


class Solution:
    def nextSmallerElementIndex(self, heights):
        n = len(heights)
        stack = []
        solution = [0] * n
        stack.append(-1)

        for i in range(n - 1, -1, -1):
            curr = heights[i]
            while stack and stack[-1] != -1 and heights[stack[-1]] >= curr:
                stack.pop()
            solution[i] = stack[-1]
            stack.append(i)

        return solution

    def prevSmallerElementIndex(self, heights):
        n = len(heights)
        stack = []
        solution = [0] * n
        stack.append(-1)

        for i in range(n):
            curr = heights[i]
            while stack and stack[-1] != -1 and heights[stack[-1]] >= curr:
                stack.pop()
            solution[i] = stack[-1]
            stack.append(i)

        return solution

    def largestRectangleArea(self, heights):
        n = len(heights)

        next_smaller = self.nextSmallerElementIndex(heights)
        prev_smaller = self.prevSmallerElementIndex(heights)

        solution = -1
        
        for i in range(n):
            height = heights[i]

            if next_smaller[i] == -1:
                next_smaller[i] = n

            width = next_smaller[i] - prev_smaller[i] - 1

            solution = max(solution, width*height)
        return solution