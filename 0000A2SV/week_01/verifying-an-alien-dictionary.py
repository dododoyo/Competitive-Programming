class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index in range(26):order_map[order[index]] = index
        for index in range(len(words)-1):
            if not self.isSorted(words[index],words[index+1],order_map):
                return False
        return True
    def isSorted(self,first_word,second_word,mp):
        i = 0
        while i < len(first_word) and i < len(second_word):
            if mp[first_word[i]] < mp[second_word[i]]:
                return True
            elif mp[first_word[i]]  > mp[second_word[i]]:
                return False
            i += 1
        return len(second_word) >= len(first_word);