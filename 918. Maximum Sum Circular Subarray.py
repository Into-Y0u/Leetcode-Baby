class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        temp_mn = temp_mx = mx = mn = sm = nums[0]
        for i in range(1,len(nums)):
            sm += nums[i]
            temp_mx = max(nums[i] , temp_mx + nums[i])
            mx = max(temp_mx , mx)
            
            temp_mn = min(nums[i] , temp_mn + nums[i])
            mn = min(temp_mn , mn)
        if sm == mn :
            return mx
        return max(mx, sm - mn)
