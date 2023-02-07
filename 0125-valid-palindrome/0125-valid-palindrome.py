#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #lets use two pointer pointed at and and begining
        # to check if characters at pointer are same
        startPointer = 0
        
        s = re.sub("[^a-z0-9]", "", s.lower())
        
        endPointer = len(s) - 1
        print(s)
        while (startPointer < endPointer):  
            if(s[startPointer] == s[endPointer]):
                startPointer += 1
                endPointer -= 1
            else:
                return False
           
        return True



        
# @lc code=end

