#backtarck N*2^n solution

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s,path):
            if not s :
                res.append(path[:])
                return 
            for i in range(1,len(s)+1):
                if s[:i] == s[i-1::-1]:
                    path.append(s[:i])
                    dfs(s[i:],path)
                    path.pop()

        
        
    res = []
    dfs(s,[])
    return res
