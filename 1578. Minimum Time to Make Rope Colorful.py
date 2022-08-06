class Solution:
    def minCost(self, cols: str, nums: List[int]) -> int:
        res = 0
        l = 0
        
        for r in range(1,len(cols)):
            if cols[l] == cols[r]:
                if nums[l] < nums[r]:
                    res += nums[l]
                    l = r
                else :
                    res += nums[r]
                    continue
            else :
                l = r
        return res
