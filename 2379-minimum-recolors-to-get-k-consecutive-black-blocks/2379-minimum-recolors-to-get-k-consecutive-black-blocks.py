class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #bruteforce approach
        swaps = k
        for i in range(len(blocks)-k+1):
            swaps = min(swaps,blocks[i:i+k].count('W'))
        return swaps