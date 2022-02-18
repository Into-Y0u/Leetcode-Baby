class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0 , len(nums)-1
        while l < r :
            mid1 = (l+r) // 2 
            mid2 = mid1+1
            if nums[mid1] < nums[mid2]:
                l = mid2
            else :
                r = mid1
        return l
