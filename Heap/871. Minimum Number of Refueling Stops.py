#    O(nlogn)

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, st: List[List[int]]) -> int:
        q = []
        new , i  = 0, 0 
        while startFuel < target :
            while i < len(st) and st[i][0] <= startFuel :
                heapq.heappush(q,-st[i][1])
                i+=1
            if not q :
                return -1
            startFuel += -heapq.heappop(q)
            new+=1
        return new
