class Solution:
    def isHappy(self, n: int) -> bool:
        arr = [n]
        vis = set()
        vis.add(n)
        while True :
            sm = 0 
            while n > 0 :
                sm += ( n%10 )**2
                n = n // 10 
            if sm == 1 :
                return 1 
            elif sm in vis :
                return 0
            else :
                vis.add(sm)
                n = sm 
