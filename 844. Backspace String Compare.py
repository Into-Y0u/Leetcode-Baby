class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def delete(arr):
            res = []
            c = 0 
            for i in range(len(arr)-1,-1,-1):
                if arr[i] == "#":
                    c+=1
                else :
                    if c == 0 :
                        res += arr[i]
                    else :
                        c-=1
            return res
        return delete(s) == delete(t)
                        
