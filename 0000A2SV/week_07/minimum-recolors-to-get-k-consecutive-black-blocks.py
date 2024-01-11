class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        max_blacks = float('inf')
        current_blacks = 0
        for right in range(len(blocks)):
            if right < k:
                current_blacks += blocks[right] == "B"
                max_blacks = current_blacks
            else:
                current_blacks -= (blocks[right] == "W" and blocks[right-k] == "B")
                current_blacks += (blocks[right] == "B" and blocks[right-k] == "W")
                max_blacks = max(max_blacks,current_blacks)
        if max_blacks < k:
            return k-max_blacks
        else:
            return 0

