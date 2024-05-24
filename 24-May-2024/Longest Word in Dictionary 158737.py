# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.EOW = False
    def hasChild(self,char):
        char_index = ord(char)-ord("a")
        return self.children[char_index] != None
    def goTo(self,char):
        char_index = ord(char)-ord("a")
        return self.children[char_index]
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insertWord(self,word):
        currentNode = self.root
        for char in word:
            char_index = ord(char)-ord("a")
            if not currentNode.hasChild(char):
                currentNode.children[char_index] = TrieNode()
            currentNode = currentNode.goTo(char)
        currentNode.EOW = True
    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if not current_node.hasChild(char):
                return False
            current_node = current_node.goTo(char)
        return current_node.EOW

    def isValid(self,word):
        for i in range(len(word)):
            sub = word[:i+1]
            if not self.search(sub):
                return False
        return True

    def findLongestWord(self):
        def dfs(currentNode,char_index):
            if currentNode == None:
                return []

            longest = []
            for i in range(26):
                child = currentNode.children[i]
                current = dfs(child,i)
                if len(current) > len(longest):
                    longest = current
            longest = [chr(char_index+97)] + longest
            return longest

        return dfs(self.root,0)


class Solution:
    def longestWord(self, words: List[str]) -> str:
        solutionTrie = Trie()
        for word in words:
            solutionTrie.insertWord(word)

        longest = ""
        for word in words:
            if solutionTrie.isValid(word):
                if len(word) > len(longest):
                    longest = word
                elif len(word) == len(longest) and word < longest:
                    longest = word
        
        return longest
        