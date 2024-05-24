# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False

    def hasChild(self,char):
        char_index = ord(char) - ord("a")
        return self.children[char_index] != None

    def addChild(self,char):
        char_index = ord(char) - ord("a")
        self.children[char_index] = TrieNode()

    def goTo(self,char):
        if char == ".":
            return None

        char_index = ord(char) - ord("a")
        return self.children[char_index]

    def setEnd(self):
        self.is_end = True
    

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        currentNode = self.root
        for char in word:
            if char != ".":
                if not currentNode.hasChild(char):
                    currentNode.addChild(char)
            currentNode = currentNode.goTo(char)
        currentNode.setEnd()
        
    def search(self, word: str) -> bool:
        
        return self.dfs(word, self.root)   

    
    def dfs(self, word, node, index = 0) -> bool:
        
        if not node: 
            return False
        if index == len(word): 
            return node.is_end

        if word[index] == '.': 
            for child in node.children:
                if self.dfs(word,child,index+1):
                    return True

        return self.dfs(word, node.goTo(word[index]), index+1)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)