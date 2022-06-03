class NumMatrix:

    def __init__(self, mat: List[List[int]]):
        row = len(mat)
        col = len(mat[0])
        
        self.dp = [[0]*(col+1) for _ in range(row+1)]
        
        for i in range(row):
            prefix = 0 
            for j in range(col):
                prefix += mat[i][j]
                above = self.dp[i][j+1]
                self.dp[i+1][j+1] = prefix + above 
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,row2,col1,col2 = row1+1,row2+1,col1+1,col2+1
        bottomRight = self.dp[row2][col2]
        topLeft = self.dp[row1-1][col1-1]
        above = self.dp[row1-1][col2]
        left = self.dp[row2][col1-1]
        return bottomRight - above - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
