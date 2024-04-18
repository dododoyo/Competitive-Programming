# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_map = Counter(words)
        word_freq = [[-val,key] for key,val in word_map.items()]
        heapq.heapify(word_freq)

        return [heapq.heappop(word_freq)[1] for _ in range(k)]