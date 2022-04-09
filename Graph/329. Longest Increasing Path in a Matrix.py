class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        row,col = len(mat),len(mat[0])

        dp  = {}
        
        def dfs(r,c,prev):
               
            if ( r<0 or c<0 or r >= row or c >= col or mat[r][c] <= prev):
                return 0 
            if dp.get((r,c)) :
                return dp[(r,c)]
            res = 1 
            res = max(res , 1 +  dfs(r+1,c,mat[r][c]))
            res = max(res , 1 +  dfs(r,c-1,mat[r][c]))
            res = max(res , 1 +  dfs(r,c+1,mat[r][c]))
            res = max(res , 1 +  dfs(r-1,c,mat[r][c]))

            dp[(r,c)] = res 
            return res
        

        for i in range(row):
            for j in range(col):
                dfs(i,j,-1)
        return max(dp.values())
        
