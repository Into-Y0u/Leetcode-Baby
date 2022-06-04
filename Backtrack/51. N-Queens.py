class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        negDiagonal = set()               # r-c will be constant
        posDiagonal = set()              # r+c will be constant
        
        res = []
        board = [["."]*n for _ in range(n)]
        
        def backtrack(r):
            if r == n :
                copy = ["".join(ele) for ele in board]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in col or r+c in posDiagonal or r-c in negDiagonal:
                    continue
                
                col.add(c)
                posDiagonal.add(r+c)
                negDiagonal.add(r-c)
                board[r][c] = "Q"
                
                backtrack(r+1)
                col.remove(c)
                posDiagonal.remove(r+c)
                negDiagonal.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res
