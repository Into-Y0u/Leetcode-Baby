class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == 0  and len(num) <= k :
            return "0"
        
        st = [num[0]]
        i = 1
        while i < len(num):
            while len(st) > 0 and int(st[-1]) > int(num[i]) and k > 0:
                st.pop()
                k-=1
            st.append(num[i])
            i+=1
            
        while k > 0 :
            st.pop()
            k-=1
        
        while  len(st) > 0 and st[0] == "0" :
            st.pop(0)
        
        if len(st) == 0 :
            return "0"
        else :
            return "".join(st)
            

            
            
            
#python special

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        
        ans = stack[:-k] if k else stack
        return "".join(ans).lstrip('0') or "0"
