class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
             
        dicu = {0:-1}
        cur = 0 
        for i,n in enumerate(nums) :
            cur += n
            left = cur % k
            if left in dicu :
                if (i - dicu[left] ) > 1 :
                    return 1
            else :
                dicu[left] = i
        return  0
