class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dicu = dict()
        for ele in words :
            if dicu.get(ele) :
                dicu[ele] += 1
            else :
                dicu[ele] = 1 
        
        res  = sorted(dicu,key = lambda x : (-dicu[x],x))
        # print(res)
        return res[:k]
