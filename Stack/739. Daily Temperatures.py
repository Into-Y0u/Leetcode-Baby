class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        dp = [0] *len(temp)
        
        st = []
        for i,n in enumerate(temp):
            while st and temp[st[-1]] < n :
                x =  st.pop()
                dp[x]  = i - x 
            st.append(i)
        return dp
