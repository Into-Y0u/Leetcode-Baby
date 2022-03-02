class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i] :
                continue
            
            l,r = i+1 , len(nums)-1
            while l < r :
                x  = nums[i] + nums[l] + nums[r] 
                if  x == 0 :
                    res.add(tuple([ nums[i],nums[l],nums[r]]))
                    l+=1
                    while l < r and nums[l-1] == nums[l]:
                        l+=1
                elif x > 0 :
                    r-=1
                else :
                    l+=1
        return res
