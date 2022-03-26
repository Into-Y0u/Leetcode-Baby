class Solution:
    def wiggleSort(self, nums):
        for i in range(1,len(nums)):
            if ((i%2==1 and nums[i-1]>nums[i]) or (i%2==0 and nums[i-1]<nums[i])   ) :
                nums[i-1] , nums[i] = nums[i] , nums[i-1] 
        return nums
