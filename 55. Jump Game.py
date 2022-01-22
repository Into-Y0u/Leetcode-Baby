class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if reach < i :
                return False         #failed to reach 
            reach = max(reach , i + nums[i])
        
        return True    #means you have reached
