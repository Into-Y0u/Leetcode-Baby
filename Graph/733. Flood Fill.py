from collections import deque
class Solution:
    def floodFill(self, img: List[List[int]], sr: int, sc: int, new: int) -> List[List[int]]:
        
        q = deque()
        yo = img[sr][sc]
        img[sr][sc] = new 
        q.append([sr,sc])
        vis = set()
        vis.add((sr,sc))
        
        while q :
            x,y = q.popleft()
            dir = [(0,1), (-1,0),(1,0),(0,-1) ]
            for dr,dc in dir :
                r = x + dr 
                c = y + dc
                
                if r in range(len(img)) and c in range(len(img[0])) and img[r][c] == yo and (r,c) not in vis :
                    img[r][c] = new 
                    vis.add((r,c))
                    q.append([r,c])
        return img
                    
        
        
