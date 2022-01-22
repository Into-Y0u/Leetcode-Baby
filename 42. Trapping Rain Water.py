class Solution:
    def trap(self, height: List[int]) -> int:
        l,r,leftmax,rightmax = 0,len(height)-1 , 0,0 
        res = 0
        while l < r :
            if height[l] <= height[r]:
                if height[l] > leftmax :
                    leftmax = height[l]
                else :
                    res += leftmax-height[l]
                l+=1
            else :
                if height[r] > rightmax :
                    rightmax = height[r]
                else :
                    res += rightmax-height[r]
                r-=1
        return res
                
