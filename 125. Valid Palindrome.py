class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join([w.lower() for w in s if w.isalnum()])
        return res == res[::-1]
   
