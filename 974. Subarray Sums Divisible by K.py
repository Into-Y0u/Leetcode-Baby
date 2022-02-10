class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cur = 0
        res = 0
        dicu = {0:1}
        for n in nums :
            cur += n
            diff = cur % k 
            res += dicu.get(diff,0)
            dicu[diff] = 1 + dicu.get(diff,0)
        return res
