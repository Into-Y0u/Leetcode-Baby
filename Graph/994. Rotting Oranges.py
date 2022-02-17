from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid : return 0
        q = deque()
        day,fresh = 0,0
        ROWS , COLS = len(grid) , len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 :
                    fresh+=1
                if grid[i][j] == 2 :
                    q.append([i,j])
        
        directions = [[0,1] ,[0,-1] , [1,0] , [-1,0] ]
        while q and fresh > 0 :
            ql = len(q)
            for i in range(ql):
                x,y = q.popleft()
                for dr,dc in directions:
                    r = x+dr
                    c = y + dc
                    if (r < 0 or r == len(grid) or c < 0 or c == len(grid[0])) or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2 
                    q.append([r,c])
                    fresh -=1
            day +=1 
        return day if fresh == 0 else -1
               
