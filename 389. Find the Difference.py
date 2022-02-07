class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "":
            return t
        if t == "" :
            return s
        dicu = dict()
        for i in s :
            if dicu.get(i) :
                dicu[i] += 1
            else :
                dicu[i] = 1 
        
        for i in t :
            if dicu.get(i) :
                dicu[i] -= 1
            else :
                dicu[i] = -1
        print(dicu)
        for i,n in dicu.items() :
            if abs(n) == 1 :
                return i
        return ""
