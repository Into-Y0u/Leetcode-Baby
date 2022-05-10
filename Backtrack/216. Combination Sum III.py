class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k*(k+1)//2 < 0 :
            return []
        elif k*(k+1)//2 == 0 :
            return [i for i in range(1,n+1)] 
        
        res = []
        
        def helper(cur,arr,t):
            if t == 0 :
                if len(cur) == k :
                    res.append(cur)
                else :
                    return 
            elif t < 0 :
                return 
            if len(cur) == k :
                if t>0 :
                    return
            
            for i,ele in enumerate(arr):
                helper(cur+[ele],arr[i+1:],t-ele)
            
            
            
            
        helper([],list(range(1,10)),n)
        return res
        
