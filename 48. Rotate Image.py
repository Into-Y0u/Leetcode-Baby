class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        l,i,n = 0 , len(m)//2 , len(m)
        
        while i > 0 :
            for p in range(l,n-1-l) :
                m[l][p], m[n-1-p][l] , m[n-1-l][n-1-p] , m[p][n-1-l] =  m[n-1-p][l] , m[n-1-l][n-1-p] , m[p][n-1-l] ,m[l][p]
            i-=1
            l+=1
        
