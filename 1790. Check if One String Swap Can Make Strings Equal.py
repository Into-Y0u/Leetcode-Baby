class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        dif = 0
        ex1 = []
        ex2 = []
        if s1 ==s2 :
            return 1
        for i in range(len(s1)):
            if s1[i] != s2[i] :
                ex1.append(s1[i])
                ex2.append(s2[i])
                dif += 1
                if dif > 2 :
                    return 0 
        if dif == 2 and ex1[0] == ex2[1] and  ex2[0] == ex1[1]:
            return 1
        else :
            return 0
        
