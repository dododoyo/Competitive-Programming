# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        mn = heappushpop(self.min_heap, num)
        heappush(self.max_heap, -mn)
        
        if len(self.max_heap) > len(self.min_heap):
            mx = heappop(self.max_heap)
            heappush(self.min_heap, -mx)
        

    def findMedian(self) -> float:
        has_even = (len(self.max_heap) == len(self.min_heap))

        if has_even:
            return (-self.max_heap[0] + self.min_heap[0]) / 2

        return self.min_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()