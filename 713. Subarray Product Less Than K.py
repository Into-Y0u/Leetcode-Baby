class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1 :
            return 0
        prod =1 
        res = 0 
        i,j = 0, 0
        while j < len(nums):
            prod *= nums[j]
            if prod < k :
                res += (j-i+1)
            elif prod >= k :
                while prod >= k :
                    prod  = prod//nums[i]
                    i+=1
                res += j-i+1
            j+=1
        return res
