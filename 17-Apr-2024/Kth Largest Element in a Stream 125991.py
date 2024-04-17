# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap,self.k = nums,k
        heapq.heapify(self.minHeap)
        # make sure the heap is size of k 

        while len(self.minHeap) > k:
            # pop the minimum untill it becomes size k 
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # we need to pop from our heap while it's length is 
        # greater than "k" because we only need a minheap of size k

        # push the new val into the heap
        heapq.heappush(self.minHeap,val)

        # pop the minimums until it becomes of size k 
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)