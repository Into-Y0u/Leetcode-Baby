class Solution:
    def findOrder(self, n: int, prereq: List[List[int]]) -> List[int]:
        dicu = {i:[] for i in range(n)}
        for crs,pre in prereq:
            dicu[crs].append(pre)
            
        res = [] ; cycle =set() ; vis = set()
        def dfs(crs) :
            if crs in cycle :
                return 0
            if crs in vis : return 1 
            
            cycle.add(crs)
            
            for pre in dicu[crs]:
                if dfs(pre) == 0 :
                    return 0
            cycle.remove(crs)
            vis.add(crs)
            res.append(crs)
            
            return res
            
            
            
            
        for c in range(n):
            if dfs(c) == False :
                return []
        return res
