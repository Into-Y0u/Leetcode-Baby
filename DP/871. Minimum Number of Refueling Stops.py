class Solution:
    def minRefuelStops(self, target: int, startFuel: int, st: List[List[int]]) -> int:
        dp = [startFuel]  +  [0]*len(st)
        for i,(pos,cap) in enumerate(st) :
            for j in range(i,-1,-1) :
                if dp[j] >= pos:
                    dp[j+1] = max(dp[j+1] , dp[j] + cap)
        # print(dp)
        for i,val in enumerate(dp) :
            if val>= target :
                return i
        return -1
    
