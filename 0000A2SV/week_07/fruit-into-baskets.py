from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # question asks to find the longest subarray 
        # with exactly two distinct elements

        elements_freq = defaultdict(int)
        left,max_sum = 0,0
        for right in range(len(fruits)):
            elements_freq[fruits[right]] += 1
            while len(elements_freq) > 2:
                elements_freq[fruits[left]] -= 1
                if elements_freq[fruits[left]] == 0:
                    elements_freq.pop(fruits[left])
                left += 1
            max_sum = max(max_sum,right-left+1)
        return max_sum


        