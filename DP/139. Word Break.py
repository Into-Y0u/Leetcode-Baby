class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        
        for i in range(n -1 ,-1 , -1):
            for w in wordDict :
                y=len(w)
                if (i + y) <= n and s[i:i+y] == w :
                    dp[i] = dp[i+y]
                if dp[i] :
                    break
        return dp[0]
