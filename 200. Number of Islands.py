from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 : return 0
        res = 0
        row,col = len(grid) , len(grid[0])
        vis = set()
        def bfs(r,c) :
            q = deque()
            q.append((r,c))
            
            while q :
                row1,col1 = q.popleft()
                directions = [(0,1),(-1,0),(1,0),(0,-1) ]
                for dr,dc in directions :
                    x,y = row1 + dr , col1 + dc
                    if   x in range(row) and y in range(col) and grid[x][y] == "1" and (x,y) not in vis :
                        vis.add((x,y))
                        q.append((x,y))
                        
                        
        for r in range(row) :
            for c in range(col) :
                if grid[r][c] == "1" and (r,c) not in vis :
                    vis.add((r,c))
                    bfs(r,c)
                    res+=1
        return res
                    
                    
        
