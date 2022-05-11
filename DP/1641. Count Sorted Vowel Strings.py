class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1]*5 for i in range(n)]
        
        for i in range(1,n):
            for j in range(4,-1,-1):
                if j == 4 :
                    dp[i][j] = dp[i-1][j]
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j+1]
        return sum(dp[-1])
            
