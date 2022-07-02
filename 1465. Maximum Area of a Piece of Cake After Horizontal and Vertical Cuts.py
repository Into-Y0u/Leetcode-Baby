class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        horizontalCuts = [0] + horizontalCuts + [h]
        
        verticalCuts = [0] + verticalCuts + [w]
        
        mx_h,mx_w = 0,0 
        for i in range(1,len(horizontalCuts)):
            mx_h = max(mx_h , horizontalCuts[i]-horizontalCuts[i-1])
            
        for i in range(1,len(verticalCuts)):
            mx_w = max(mx_w , verticalCuts[i]-verticalCuts[i-1])
        
        return (mx_h * mx_w)%(10**9 + 7)
