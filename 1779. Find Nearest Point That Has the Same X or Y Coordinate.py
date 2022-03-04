import sys
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mn = sys.maxsize
        res = -1
        for i,n in enumerate(points):
            p,q = n
            if p == x or q == y :
                k = abs(x-p) + abs(y-q)
                if mn > k :
                    mn = k
                    res = i
        return res
