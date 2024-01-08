class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels,current_vowels,vowels_set  = 0,0,{'a','e','i','o','u'}
        for right in range(len(s)):
            if right < k:
                current_vowels += s[right] in vowels_set
            else:
                current_vowels += (s[right] in vowels_set) - (s[right-k] in vowels_set)
            max_vowels = max(max_vowels,current_vowels)
        return max_vowels
        