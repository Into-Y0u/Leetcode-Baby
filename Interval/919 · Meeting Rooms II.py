class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start = sorted([i.start for i in intervals] )
        end = sorted([i.end for i in intervals] )

        res,count = 0,0 
        s,e=0,0

        while s < len(start) :
            if start[s] <end[e] :
                count +=1
                s +=1
            else :
                e +=1
                count -= 1
            res = max(count,res)
        return res
