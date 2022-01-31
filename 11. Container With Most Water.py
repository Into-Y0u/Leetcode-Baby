class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0 ; end = len(height) -1 ; ans = 0 ; res = 0
        while start < end :
            width  = abs(start - end)
            if height[start] < height[end]:
                res = width * height[start]
                start +=1
            else :
                res = width * height[end]
                end -= 1
                
            ans = max(ans,res)
            
        return ans
        
