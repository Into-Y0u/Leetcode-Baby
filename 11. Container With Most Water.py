class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        cur = res = 0
        while l < r :
    
            cur = min(height[l],height[r]) * (r-l)
            if height[l] <= height[r]:
                l+=1
            else :
                r-=1
            res = max(cur,res)
        return res
            
        
        
