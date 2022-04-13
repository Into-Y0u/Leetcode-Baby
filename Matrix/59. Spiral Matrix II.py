class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for i in range(n)]
        left,right,top,bot = 0,n,0,n
              
        num = 1
               
        while left < right and top < bot:
            for i in range(left, right):
                res[top][i] = num
                num+=1
            top+=1
            
            for i in range(top,bot):
                res[i][right-1] = num
                num+=1
            
            right -=1
            
            for i in range(right-1,left-1,-1):
                res[bot-1][i] = num
                num+=1
            
            bot-=1
            
            for i in range(bot-1,top-1,-1):
                res[i][left] = num 
                num+=1
            left+=1
        return res
            
