class Solution:
    def transpose(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[0]*m for i in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i]= mat[i][j]
        
        return res
