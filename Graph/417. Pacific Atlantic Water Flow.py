class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        pac = set()
        alt = set()
        
        def dfs(r,c,vis,prev):
            if (r<0 or r>=m or c<0 or c>=n or (r,c) in vis or heights[r][c] < prev):
                return 
            vis.add((r,c))
            dfs(r+1,c,vis,heights[r][c])
            dfs(r,c-1,vis,heights[r][c])
            dfs(r-1,c,vis,heights[r][c])
            dfs(r,c+1,vis,heights[r][c])
            
            
            
        for c in range(n) :
            dfs(0,c,pac,heights[0][c] )
            dfs(m-1,c,alt,heights[m-1][c])
    
                
        for r in range(m):
            dfs(r,0,pac,heights[r][0] )
            dfs(r,n-1,alt,heights[r][n-1])
        
        res = []
        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in alt :
                    res.append([r,c])
        return res
            
        
        
        
