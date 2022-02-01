class Solution:
    def maximalSquare(self, m: List[List[str]]) -> int:
        row = len(m)
        col = len(m[0])
        dp = [[0]*(col+1) for _ in range(row+1)]

        mx = 0
        for i in range(1,row+1):
            for j in range(1,col+1):
                if m[i-1][j-1] == "1":
                    dp[i][j]  = 1 + min( dp[i-1][j-1] , dp[i-1][j] , dp[i][j-1] )
 
                    mx = max(mx ,dp[i][j] )
 
        return mx*mx
    
