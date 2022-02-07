class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        if len(nums) <= 2 : return min(nums)
        nums.append(0)
        n = len(nums)
        dp  = [-1] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in range(2,n) :
            dp[i] = min(dp[i-2] , dp[i-1]) + nums[i]
        
        return dp[n-1]
