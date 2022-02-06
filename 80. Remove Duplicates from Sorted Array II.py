class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dicu = dict()
        i = 0
        while i < len(nums) :
            if dicu.get(nums[i]) :
                if dicu[nums[i]] < 2 :
                    dicu[nums[i]] += 1
                    i+=1
                else :
                    nums.pop(i)
            else :
                dicu[nums[i]] = 1
                i+=1
        # print(nums)
        return len(nums)
