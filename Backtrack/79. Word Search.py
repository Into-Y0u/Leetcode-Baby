# time complexity : O(m*n*4^(n))    dont do this

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        vis = set()
        
        def dfs(r,c,k) :
            if k == len(word):
                return 1
            if (r < 0 or c < 0 or r >= m or  c >= n or  (r,c) in vis or  board[r][c] != word[k]) :
                return 0 
            vis.add((r,c))
            res = ( dfs(r-1,c,k+1) or dfs(r+1,c,k+1) or dfs(r,c-1,k+1) or dfs(r,c+1,k+1) )
            vis.remove((r,c))
            return res

        for i in range(m):
            for j in range(n) :
                if dfs(i,j,0):
                    return 1 
        return 0
            
