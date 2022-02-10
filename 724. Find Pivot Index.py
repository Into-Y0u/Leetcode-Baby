class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsm = 0 
        rightsm = sum(nums)
        for key,val in enumerate(nums):
            if leftsm == rightsm - val:
                return key
            leftsm += val
            rightsm -= val
            # print(leftsm,rightsm)
            
        return -1
