class Solution:
    def coinChange(self, coins: List[int], a: int) -> int:
        dp = [a+1] * (a+1)
        dp[0] = 0 
        coins.sort()
        for i in range(1,a+1):
            for j in coins:
                if i - j >=0 :
                    dp[i] = min(dp[i] , 1 + dp[i-j])
                else :
                    break
        # print(dp)
        return -1 if dp[a] == a+1 else dp[a]
