class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        shit = ["","."]
        ans = []
        for n in arr :
            if n in shit :
                continue

            if n == "..":
                if ans:
                    ans.pop()
                continue
            ans.append(n)
        return "/"+"/".join(ans) if ans else "/"
