import heapq
class Solution:
    def MinimumCost(self, sticks):
        # write your code here
        heapq.heapify(sticks)
        x = 0 ; res = 0
        while len(sticks) > 1 :
            x = heapq.heappop(sticks)
            x += heapq.heappop(sticks)
            res += x
            heapq.heappush(sticks,x)
        return res
