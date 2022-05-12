class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2 != 0 :
            return 0

        n = len(nums)
        sm = sum(nums)//2
        dp = [[0]*(sm+1) for i in range(n+1) ]
        
        
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1,n+1):
            for j in range(1,sm+1):
                if nums[i-1] <= j :
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j] 
                else :
                    dp[i][j] = dp[i-1][j]
  
        return dp[n][sm]
                    
