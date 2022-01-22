class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicu = dict()
        res = []
        for s in strs :
            sorted_s = sorted(s)
            sorted_s = tuple(sorted_s)
            if dicu.get(sorted_s) :
                dicu[sorted_s].append(s)
            else :
                dicu[sorted_s] = [s]
        # print(dicu)
        for n in dicu:
            res.append(dicu[n])
        # print(res)
        return res
