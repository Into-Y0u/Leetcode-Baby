class Solution:
    def intervalIntersection(self, arr1: List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
        i,j = 0, 0 
        res = []
        while i < len(arr1) and j < len(arr2):
            p1,q1 = arr1[i]
            p2,q2 = arr2[j]
            
            if p1 > q2 :
                j+=1
                continue
            elif p2 > q1 :
                i+=1
                continue 
            
            start = max(p1,p2)
            end = min(q1,q2)
            res.append([start,end])
            
            if q1 <= q2 :
                i+=1
            else :
                j+=1
        return res
            
