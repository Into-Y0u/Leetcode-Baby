class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero = [None] * (len(nums)+1)
        one = [None] * (len(nums)+1)
        j = 0 
        zero[0] = 0 ; one[len(nums)] = 0
        for i in range(1,len(nums)+1):
            if nums[i-1] == 0:
                j+=1
            zero[i] = j
        j=0
        for i in range(len(nums)-1,-1,-1 ):
            if nums[i] == 1:
                j+=1
            one[i] = j
        # print(zero,one)
                
        sm = 0 ; res = []
        for i in range(len(zero)):
            x = zero[i] + one[i] 
            if x > sm :
                sm = x
                res = []
                res.append(i)
            elif x == sm :
                res.append(i)
                
        return res
            

        
