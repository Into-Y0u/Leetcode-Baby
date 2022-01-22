class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1 :
            return 0
        jump = 1 
        maxreach = nums[0]
        steps = nums[0]
        for i in range(1,len(nums)):
            if i == len(nums)-1 :
                return jump 
            maxreach = max(maxreach , i + nums[i])
            steps -= 1
            if steps == 0 :
                jump+=1                                                    #if -1 options are there ; add if i >= maxreach : return -1
                steps = maxreach - i 
        return jump        
