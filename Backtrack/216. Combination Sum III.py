class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [i for i in range(1,10)] 
        target = n
        res = []
  
        
        def helper(i,cur,target) :
            if target == 0  :
                res.append(cur.copy())
                return 
            if target < 0 :
                return 
            
            for j in range(i,9) :
                
                cur.append(arr[j])
                helper(j+1 , cur , target - arr[j])
                cur.pop()
            
        helper(0,[],target)
        # print(res)
        i = 0
        while i < len(res) and res :
            if len(res[i])  == k :
                i+=1
            else :
                res.pop(i)
        return res
