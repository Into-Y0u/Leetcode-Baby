class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res =[]
        nums.sort()
        for i,a in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i] :
                continue
            
            l,r = i+1,len(nums)-1
            
            while l < r :
                sm = nums[i] + nums[l] + nums[r]
                if sm > 0  :
                    r-=1
                elif sm < 0 :
                    l+=1
                else :
                    res.append([nums[i] , nums[l] , nums[r]])
                    l+=1
                    while nums[l-1] == nums[l] and l < r :
                        l+=1
        return res
        
