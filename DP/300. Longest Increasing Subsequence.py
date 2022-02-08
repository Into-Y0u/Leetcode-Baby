# O(n**2) solution


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i in range( len(nums)):
            for j in range(i):
                if nums[i] > nums[j] :
                    dp[i] = max(dp[i] , 1 + dp[j])
        print(dp)
        return max(dp)
    
    

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j] :
                    dp[i] = max(dp[i] , 1 + dp[j])
        # print(dp)
        return max(dp)
