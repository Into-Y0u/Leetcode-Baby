class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for n in stones :
            heappush(max_heap,-n)
        
        while max_heap :
            sto1 = -heappop(max_heap)
            if not max_heap :
                return sto1
            sto2 = -heappop(max_heap) 
            diff = sto1-sto2
            if diff > 0 :
                heappush(max_heap, -diff)
        return 0
