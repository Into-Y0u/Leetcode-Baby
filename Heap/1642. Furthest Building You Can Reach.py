class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        
        for i in range(len(heights)-1):
            temp = heights[i+1] - heights[i]
            if temp <= 0 :
                continue
            heappush(heap,temp)
            if len(heap) > ladders :
                bricks -= heappop(heap)
            if bricks < 0 :
                return i
        return len(heights)-1
        
