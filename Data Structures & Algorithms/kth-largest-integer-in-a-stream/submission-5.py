import heapq
class KthLargest:
    """
    common pitfall: max heap 因為不符合時間複雜度
    maxheap - O(m · k log n) 因為add()每次都要pop+push k 次: O(k log n),而add()又可能做m次
    minheap - O(m log k) 每次鎖死在高度 = k,且由於是 minheap size k, 直接取root就是topk element
    """
    def __init__(self, k: int, nums: List[int]):
        self.k, self.nums = k, nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        
        if len(self.nums) > self.k: #不这样一開始堆size時会永远永远无法增长到 k
            heapq.heappop(self.nums)
        
        return self.nums[0]
        
