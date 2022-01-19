class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicu = dict()
        for i,n in enumerate(nums):
            temp  = target - n 
            if dicu.get(temp) :
                if dicu[temp][0] != i :
                    return [dicu[temp][0] , i] 
            dicu[n] = [i]
            
