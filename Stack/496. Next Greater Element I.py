class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dp = [0]*len(nums2)
        st  = []
        dicu = {}
        for i,n in enumerate(nums2):
            dicu[n] = i
            while st and nums2[st[-1]] < n :
                x = st.pop()
                dp[x] = i - x 
            st.append(i)
        # print(dp)
        res = [0]*len(nums1)
        for i,n in enumerate(nums1):
            loc = dicu[n] 
            y = dp[loc]
            res[i]=nums2[loc+y] if y != 0 else -1
        return res
                
