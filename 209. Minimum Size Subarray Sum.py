class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        start,sm= 0,0
        for i in range(len(nums)):
            sm+=nums[i]
            while sm >= target :
                res = min(i - start + 1 ,res)
                sm -= nums[start]
                start+=1
        return 0 if res > len(nums) else res
                
