class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=collections.Counter(s)
        print(d)
        ans=0
        flag=False
        for i in d:
            if d[i]%2!=0:
                ans+=d[i]-1
                flag=True
            else:
                ans+=d[i]

        return ans+1 if flag else ans
