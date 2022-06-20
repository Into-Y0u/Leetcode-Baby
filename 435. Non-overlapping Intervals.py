class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        print(intervals)
        
        res = 0
        prev = float("-inf")
        for x,y in intervals:
            if x >= prev :
                prev = y
            else :
                res +=1
        return res
        
