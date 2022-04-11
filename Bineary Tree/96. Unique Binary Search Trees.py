class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n+1)
        
        for nodes in range(2,n+1):
            total = 0 
            for j in range(1,nodes+1):
                left = j-1
                right = nodes - j 
                total += dp[left] * dp[right]
            dp[nodes] = total
        return dp[n]
        
