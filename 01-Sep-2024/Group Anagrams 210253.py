# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
class Solution:
    def getFreqArray(self,strng):
        freq = [0]*26
        for character in strng:
            freq[ord(character)-97] += 1
        return freq
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for strng in strs:
            freq_arr = self.getFreqArray(strng);
                
            #if frequency array in dictionary append it to it's members
            freq_tuple = tuple(freq_arr)
            if freq_tuple in anagrams:
                anagrams[freq_tuple].append(strng)
            
            #else create new array with that anagram
            else:
                anagrams[freq_tuple] = [strng]
            
        # return all the list in the dictionary
        return anagrams.values()
            