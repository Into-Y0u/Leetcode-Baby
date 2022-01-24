class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr , res = [0]*60 , 0 
        for n in time :
            res += arr[(60-n%60)%60]
            arr[n%60] += 1
        return res
