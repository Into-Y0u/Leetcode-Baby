class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack, cur = [], ""
        for c in s:
            if cur and c != cur[-1]:
                stack.append(cur)
                cur = ""
            cur += c
            while len(cur) >= k:
                if not stack:
                    cur = ""
                    break
                cur = stack.pop()
        stack.append(cur)
        return "".join(stack)
