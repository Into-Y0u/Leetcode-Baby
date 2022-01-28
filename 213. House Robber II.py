class Solution:
    def helper(self,nums) :
        if len(nums) == 1 : return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])
        
        
        return dp[-1]
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<= 2 : return max(nums)
        return max(self.helper(nums[1:]),self.helper(nums[:n-1]))
