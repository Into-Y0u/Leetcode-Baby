class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        lisLen ,res = 0 , 0
        
        for i in range(len(nums)-1,-1,-1):
            maxLen,maxCnt = 1,1
            for j in range(i+1 , len(nums)):
                if nums[j] > nums[i] :
                    length ,count = dp[j]
                    if 1 + length > maxLen :
                        maxLen = length + 1
                        maxCnt = count
                    elif 1 + length == maxLen :
                        maxCnt += count
            if maxLen > lisLen :
                lisLen,res = maxLen, maxCnt 
            elif maxLen  == lisLen :
                res += maxCnt 
            dp[i] = [maxLen  , maxCnt]
        return res
    
    
