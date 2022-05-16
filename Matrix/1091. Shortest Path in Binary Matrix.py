class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        q.append((0,0,1))
        dp = [[0]*n for i in range(n)]

        while q :
            x,y,cur = q.popleft()
            
            if not 0<= x < n or not 0<= y < n or dp[x][y] ==1 or grid[x][y] == 1 :
                continue 
            
            if x == n-1 and y == n-1 :
                if grid[x][y] == 0 :
                    return cur
                continue
          
            
            dp[x][y] =1
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    q.append((i,j,cur+1))
        return -1
                
