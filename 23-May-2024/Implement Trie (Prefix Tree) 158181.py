# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end_of_word = False
    def containsChild(self,character):
        char_index = ord(character)-ord('a')
        return self.children[char_index] != None
    def put(self,character,child):
        char_index = ord(character)-ord('a')
        self.children[char_index] = child
    def goTo(self,character):
        char_index = ord(character)-ord('a')
        return self.children[char_index]
    def setEnd(self): 
        self.end_of_word = True
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if not current_node.containsChild(char):
                current_node.put(char,TrieNode())
            current_node = current_node.goTo(char)
        current_node.setEnd()


    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if not current_node.containsChild(char):
                return False
            current_node = current_node.goTo(char)

        return current_node.end_of_word
        
    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            if not current_node.containsChild(char):
                return False
            current_node = current_node.goTo(char)
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)