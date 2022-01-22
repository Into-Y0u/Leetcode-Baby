import heapq
class Solution:
    def solve(self, A):
        A.sort()
        res = 1
        heap = [A[0][1]]
        for start,end in A[1:]:
            if  heap[0]  <= start  :
                heapq.heappop(heap)
            heapq.heappush(heap,end)
            res = max(res,len(heap))
        return res
