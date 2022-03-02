class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        p = 1 
        res = []
        for n in nums:
            res.append(p)
            p *= n
        p = 1 
        print(res)
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * p
            p *= nums[i]
        return res
        
        
            
