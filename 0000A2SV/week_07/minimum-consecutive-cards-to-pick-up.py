from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # question asks to get the longest subarray ending with same elements

        # get members seen till now (dictionary)
        # if the member[right] is in seen  while cards[left] != cards[right] ; left += 1
        left,members,min_len = 0,defaultdict(int),float('inf')
        for right in range(len(cards)):
            if cards[right] in members:
                while cards[right] != cards[left]:
                    members[cards[left]] -= 1
                    if members[cards[left]] == 0:
                        members.pop(cards[left])
                    left += 1
                min_len = min(min_len,right-left+1)
                members[cards[left]] -= 1
                left += 1
            members[cards[right]] += 1
        return min_len if min_len != float('inf') else -1
