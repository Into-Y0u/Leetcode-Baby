class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            # Check if mid is the single number
            if start < mid < end and nums[mid-1] < nums[mid] < nums[mid+1]:
                return nums[mid]
            else:
                # Else goto the second index of nums[mid](duplicate) if already not there.
                if mid < end and nums[mid] == nums[mid+1]:
                    mid += 1
            
            if (mid - start + 1) % 2:
                end = mid - 2
            else:
                start = mid + 1
        return nums[start]
