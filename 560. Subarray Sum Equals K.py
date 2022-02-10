class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur = 0 
        dicu = { 0 : 1 }
        res = 0 
        for n in nums :
            cur+=n
            diff  = cur - k 
            
            res += dicu.get(diff,0)
            dicu[cur] = 1 + dicu.get(cur,0)
        return res
