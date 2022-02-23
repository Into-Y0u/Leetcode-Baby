class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dicu = {i:[] for i in range(numCourses)}
        
        vis = set()
        
        for crs,pre in prerequisites :
            dicu[crs].append(pre)
        
        
        def dfs(crs):
            if crs in vis :
                return False
            if dicu[crs] == []:
                return True
            
            vis.add(crs)
            
            for ele in dicu[crs]:
                if not dfs(ele) : return False
            
            vis.remove(crs)
            dicu[crs] = []
            return True
        
        
        for crs in range(numCourses):
            if not dfs(crs) :
                return False
        return True
