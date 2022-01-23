class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        j = 1 
        n = len(nums)
        res = []
        nums.sort()
        i = 0
        arr = [-1] *(n + 1 )
        for n in nums :
            arr[n] = 1 
        for i in range(1,len(arr)):
            if arr[i] == -1 :
                res.append(i)
        return res
                
