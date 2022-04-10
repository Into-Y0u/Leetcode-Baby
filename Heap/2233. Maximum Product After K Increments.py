class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums :
            heappush(heap,i)
        while k :
            cur = heappop(heap)
            heappush(heap,cur+1)
            k-=1
        res = 1 
        while heap :
            cur = heappop(heap)
            res  = (res*cur) % (10**9+7)
        return res
