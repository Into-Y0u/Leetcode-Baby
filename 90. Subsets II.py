class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        
        for num in nums:
            for index in range(len(ans)):
                temp = ans[index] + [num]
                print(temp)
                if temp not in ans:
                    ans.append(temp)
        
        return ans
        
