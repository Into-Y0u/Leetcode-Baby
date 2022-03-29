class Solution:
    def reverseVowels(self, s: str) -> str:
        if s == "" or s == " ": return s
        s = list(s)
        # print(s)
        l = 0 
        r = len(s)-1
        dicu = {"a":1,"e":1, "i":1, "o":1, "u":1,"A":1,"E":1, "O":1, "I":1, "U":1}
        while l < r :
            if dicu.get(s[l]) and dicu.get(s[r]):
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
            elif dicu.get(s[l]) :
                r-=1
            elif dicu.get(s[r]) :
                l+=1
            else :
                l+=1
        return "".join(s)
