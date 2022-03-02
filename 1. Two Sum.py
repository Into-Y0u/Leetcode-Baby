class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicu = {}
        for i, n in enumerate(nums):
            if (target-n) in dicu :
                return [dicu[target-n] , i ]
            else :
                dicu[n] = i
        
