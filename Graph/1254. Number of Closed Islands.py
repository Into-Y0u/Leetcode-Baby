class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[0]*n for i in range(m)]
        res = 0
        
        def bfs(i,j):
            vis[i][j] = 1
            q = [(i,j)]
            valid = 1
            
            while len(q)> 0 :
                r,c = q.pop(0)
                if r == 0 or r == m-1 or c == 0 or c == n-1 :
                    valid = 0
                dire = [(1,0),(0,-1),(0,1),(-1,0)]
                for dx,dy in dire:
                    x = r + dx
                    y = c+ dy
                    if 0<=x<m and 0<=y<n and grid[x][y] == 0 and not vis[x][y] :
                        vis[x][y] = 1
                        q.append((x,y))
            return valid
            
            
        
        
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == 0 :
                    if bfs(i,j):
                        res += 1
        return res
