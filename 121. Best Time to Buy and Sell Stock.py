class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mn = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < mn :
                mn = prices[i]
            res = max(res, prices[i] - mn)
        return res
