from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # c = list(Counter(arr).items())
        c = Counter(arr)
        z = sorted(c.items(),key = lambda x : x[1],reverse = True)
        # print(z)
        while len(z) >= 1 and k > 0 :
            x = z[-1][1]
            # print(x)
            if x <=  k :
                z.pop()
                k-=x
            else :
                break
        return len(z)
