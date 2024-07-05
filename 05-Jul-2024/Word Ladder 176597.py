# Problem: Word Ladder - https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        begin = list(beginWord)

        current_level = [[begin,1]]
        wordSet = set(wordList)
        n = len(beginWord)

        while current_level:
            next_level = []
            for word,change in current_level:
                for i in range(n):
                    new = word[:]
                    # change word at index i from "a" to "z"
                    for j in range(97,123):
                        new[i] = chr(j)
                        if new != word:
                            strWord = "".join(new) 
                            if strWord in wordSet:
                                if strWord == endWord:
                                    return change+1

                                next_level.append([new[:],change+1])
                                wordSet.remove(strWord)
                                
            current_level = next_level[:]

        # Time : O((len(wordList))*26*(n))
        # Space : O(len(wordList)*n)
        return 0
