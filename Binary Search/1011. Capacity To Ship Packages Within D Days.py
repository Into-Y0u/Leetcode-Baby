class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        mx,sm = 0,0
        for ele in weights :
            if ele > mx :
                mx = ele 
            sm += ele 
        def yo(cap) :
            days = 1 
            local = 0
            for  w in weights :
                local += w
                if local > cap :
                    local = w 
                    days+=1
                    if days > D :
                        return 0
            return 1
            
        
        left,right = mx , sm 
        while left < right :
            mid = left + (right-left)//2
            if yo(mid):
                right = mid 
            else :
                left  = mid+1
        return left
            
