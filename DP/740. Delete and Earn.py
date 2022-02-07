class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dicu = dict()
        for n in nums :
            if dicu.get(n) :
                dicu[n] +=1
            else :
                dicu[n] = 1 
                
        arr = list(set(nums))
        arr.sort()
        # print(arr)
        n = len(arr)
        dp = [0] * n
        
        e1,e2 = 0,0
        for i in range(n):
            cur = dicu[arr[i]] * arr[i]
            tmp = e2
            if i > 0 and arr[i] == arr[i-1] + 1 :
                e2 = max(e2 , e1 + cur)
            else :
                e2 += cur 
                
            e1 = tmp
        return e2
        
