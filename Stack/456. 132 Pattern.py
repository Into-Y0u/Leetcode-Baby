class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st = []
        s2 = -float('inf')
        for c in nums[::-1]:
            if c < s2 :
                return 1 
            while st and st[-1] < c :
                s2 = st.pop()
            st.append(c)
        return 0
