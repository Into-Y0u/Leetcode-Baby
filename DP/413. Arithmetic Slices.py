class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [0]*(n-1)
        
        for i in range(1,n):
            dp[i-1] = nums[i] - nums[i-1]
            
        # print(*dp)
        m = 1 
        res = 0
        for i in range(1,len(dp)):
            if dp[i-1] == dp[i] :
                res+=m
                m+=1
            else :
                m = 1 
        return res
        
