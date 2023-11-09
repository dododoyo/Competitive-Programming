class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastIndex = dict()
        for index,number in enumerate(nums):
            if number in lastIndex and (abs(lastIndex[number] - index)) <= k:
                return True
            else:
                lastIndex[number] = index
            # print(lastIndex)
        return False