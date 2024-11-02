# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None]*2
        self.EON = False

    def containsChild(self,bit):
        if bit == "0":
            return self.children[0] != None
        else:
            return self.children[1] != None
    def put(self,bit):
        if bit == "0":
            self.children[0] = TrieNode()
        else:
            self.children[1] = TrieNode()
    def goTo(self,bit):
        if bit == "0":
            return self.children[0]
        else:
            return self.children[1]
    def setEnd(self): 
        self.EON = True
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, bitArray: str) -> None:
        current_node = self.root
        for bit in bitArray:
            if not current_node.containsChild(bit):
                current_node.put(bit)
            current_node = current_node.goTo(bit)
        current_node.setEnd()

    def findMaxXOR(self, bitArray):
        solution = 0
        current_node = self.root
        for index in range(32):
            if bitArray[index] == "0":
                if current_node.containsChild("1"):
                    solution |= (1<<(31-index))
                    current_node = current_node.goTo("1")
                else:
                    current_node = current_node.goTo("0")  
            else:
                if current_node.containsChild("0"):
                    solution |= (1<<(31-index))
                    current_node = current_node.goTo("0") 
                else:
                    current_node = current_node.goTo("1")
        return solution
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        solutionTrie = Trie()
        final_solution = 0
        for number in nums:
            binary = format(number, '032b')
            solutionTrie.insert(binary)
        
        for number in nums:
            binary = format(number, '032b')
            current_solution = solutionTrie.findMaxXOR(binary)
            final_solution = max(final_solution,current_solution)
            
        return final_solution

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)