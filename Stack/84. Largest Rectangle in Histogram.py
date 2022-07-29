class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        res = 0
        st = [-1]
        n = len(heights)
        
        for i in range(n):
            while heights[i] < heights[st[-1]] :
                h = heights[st.pop()]
                w = i - 1 - st[-1]
                res = max(res,h*w)
            st.append(i)
        return res
