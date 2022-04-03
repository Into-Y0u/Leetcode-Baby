class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1 
        while i > 0 :
            if nums[i] > nums[i-1] :
                break
            i-=1
        if i == 0 :
            nums.reverse()
            return nums 
        
        brk_point  = i-1
        for j in range(i,n-1):
            for k in range(j,n):
                if nums[j] > nums[k] :
                    nums[j],nums[k] = nums[k],nums[j]
        # print(nums)
        for i in range(brk_point,n):
            if nums[brk_point] < nums[i]:
                nums[brk_point] , nums[i] = nums[i] ,nums[brk_point] 
                break
        return nums
                
