class Solution:
    def findCircleNum(self, arr: List[List[int]]) -> int:
        def dfs(start):
            vis.add(start)
            for end in range(len(arr)):
                if end not in vis and arr[start][end] :
                    dfs(end)
                    
            
        res = 0
        n = len(arr)
        vis = set()
        for start in range(len(arr)):
            if start not in vis :
                res+=1
                dfs(start)
                
        
        return res
    
        
