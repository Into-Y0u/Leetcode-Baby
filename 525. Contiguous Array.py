class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dicu = {0:-1}
        pre,res = 0 , 0
        for i in range(len(nums)):
            pre += 1 if nums[i] else -1 
            if pre in dicu:
                res = max(res,i-dicu[pre])
            else :
                dicu[pre] = i
        return res
