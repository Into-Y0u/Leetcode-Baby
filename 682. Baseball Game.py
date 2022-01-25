class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for n in ops :
            if n == "+":
                res.append(res[-1] + res[-2])
            elif n == "D" :
                x = res[-1]
                res.append(x*2)
            elif n == "C" :
                res.pop()
            else :
                res.append(int(n))
            # print(res)
        return sum(res)
                
