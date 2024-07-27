# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        temp = []
        for i in range(len(nums)):
            n,x = str(nums[i]),""
            for j in range(len(n)):
                if x or mapping[int(n[j])]:
                    x += str(mapping[int(n[j])])
            temp.append(int(x if x else "0"))
        
        map = defaultdict(int)
        for i in range(len(nums)):
            map[(temp[i], i) ] = nums[i]

        return [item[1] for item in sorted(map.items())]
    