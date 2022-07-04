class Solution:
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:
        n = len(start)
        jobs = sorted(list(zip(start,end,profit)) , key = lambda x : x[1])
        
        dp = [0]*n
        dp[0] = jobs[0][2]
        
        for i in range(1,n):
            prev = dp[i-1]
            increment = jobs[i][2] 
            
            for j in range(i-1,-1,-1):
                if jobs[i][0] >= jobs[j][1]:  #checking if start time is greater than prev end time
                    increment += dp[j]
                    break
            dp[i] = max(prev , increment)
        return dp[-1]
            
