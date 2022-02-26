

# better Runtime 168ms <Recursive 😁👻👻👻>
class Solution:
    def dfs(self,grid,r,c) :
        num = 1 
        grid[r][c] = 0 
        
        directions = [(r+1, c),(r-1, c),(r, c-1),(r, c+1) ]
        for x,y in directions :
            if x in range(len(grid)) and y in range(len(grid[0])) and grid[x][y] == 1 :
                
                num+= self.dfs(grid,x,y)
        return num
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid : return 0
        row , col = len(grid) , len(grid[0])
        
        res = 0 
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 :
                    res = max(res, self.dfs(grid,i,j))
        return res
  
  
 
 
 # Iterative 228ms 😐😐😐😐😐😐😐😐😐😐😐😐
 
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid : return 0
        row,col = len(grid),len(grid[0])
        vis = set()
        res = 0
        def dfs(r,c):
            num  = 1
            q = deque()
            q.append([r,c])
            while q :
                x,y = q.popleft()
                dir = [(0,1),(-1,0),(1,0),(0,-1) ]
                for dr , dc in dir :
                    m = x + dr
                    n = y + dc 
                    if m in range(row) and n in range(col) and grid[m][n] == 1 and (m,n) not in vis :
                        
                        vis.add((m,n))
                        q.append([m,n])
                        num+=1
            return num
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in vis :
                    vis.add((i,j))
                    cur = dfs(i,j)
                    res = max(cur,res)
                    print(cur,res)

        return res
        
