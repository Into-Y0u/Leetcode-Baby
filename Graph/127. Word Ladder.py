from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, b: str, e: str, wl: List[str]) -> int:
        if e not in wl : return 0
        
        nei = defaultdict(list)
        
        wl.append(b)
        q = deque([b])                #this is the turning point
        res = 1

        for w in wl :
            for j in range(len(w)):
                pat = w[:j] + "*" + w[j+1:] 
                nei[pat].append(w)

        vis = set()
        while q :
            
            for i in range(len(q)):
                w = q.popleft()
                print(w)
                if w == e :
                    return res
                for j in range(len(w)):
                    pat = w[:j] + "*" + w[j+1:] 
                    for neyo in nei[pat] :
                        if neyo not in vis :
                            vis.add(neyo)
                            q.append(neyo)
            res+=1
        return 0
                        

                
