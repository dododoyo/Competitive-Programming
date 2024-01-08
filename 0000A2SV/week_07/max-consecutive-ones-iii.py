class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0 
        for right in range(len(nums)):
            # decreamenting k signifies we used
            # one of our chances of changing 0 -> 1
            if nums[right] == 0: 
                k -= 1

            # k is less than zero means we have
            # used more chances than we are given
            # some we must remove one element
            if k < 0:
                left += 1   #removing the element

                # but we have to keep in mind that if the removed 
                # element is zero, that means we gain back the life 
                # we used for flipping that zero
                if nums[left-1] == 0:k += 1

        return right-left+1