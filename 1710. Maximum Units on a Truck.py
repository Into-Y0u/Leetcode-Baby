class Solution:
    def maximumUnits(self, box: List[List[int]], t: int) -> int:
        box.sort(key = lambda x : x[1] , reverse = True)
        res = 0
        for n,b in box :
            temp = min(t,n)
            res += temp * b 
            t -= temp 
            if t == 0 :
                break 
            
        return res
        
