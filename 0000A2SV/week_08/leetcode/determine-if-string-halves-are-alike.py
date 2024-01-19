class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels,vowels_count = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'},0
        for char in s:vowels_count += (char in vowels)
        # if vowels are odd it can't be divided to two
        if vowels_count%2:return False
        # count half of the string for vowels
        half_vowel_count = 0
        for i in range(len(s)//2):
            half_vowel_count += s[i] in vowels
        # if the vowels in half of the string is equal
        # to the number of vowels in half of the string
        if half_vowel_count == vowels_count//2:
            return True
        else:
            return False
        