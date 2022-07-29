class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        res = [-1] * n
        
        st = []
        for j in range(2):
            for i in range(n):
                while st and (nums[st[-1]] < nums[i]) :
                    res[st.pop()] = nums[i]

                st.append(i)
        return res
            
