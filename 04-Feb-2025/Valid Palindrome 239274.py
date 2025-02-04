# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filter alphanumeric 
        filtered = []
        for char in s:
            if char.isalnum():
                filtered.append(char.lower())
        # print(filtered)
        return filtered == filtered[::-1]
        