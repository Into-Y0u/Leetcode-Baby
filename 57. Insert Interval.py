class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.extend([newInterval])
        intervals.sort()
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                if intervals[i][1] > intervals[i-1][1]:
                    intervals[i-1][1] = intervals[i][1]
                intervals.pop(i)
            else :
                i+=1
        return intervals
