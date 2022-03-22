class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(a,b):
            if a==0 :
                return b
            return gcd(b%a,a)
        def lcm(a,b):
            return (a*b) // gcd(a,b)
        
        
        left,right = 1 , n*min(a,b)
        ans = 0
        while left <= right :
            mid = (left+right)//2
            target = (mid//a) + (mid//b) - (mid//lcm(a,b))
            if target < n :
                left = mid+1
            else :
                right = mid -1 
                ans = mid
        return ans%(10**9+ 7)
                
