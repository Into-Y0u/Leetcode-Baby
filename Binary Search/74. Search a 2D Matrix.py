class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        if not mat : return -1
        def search(nums, target):
            if len(nums) == 1 and nums[0] == target :
                return 0
            l,r = 0, len(nums)-1
            while l <= r :
                mid = l + (r-l)//2
                if nums[mid] == target :
                    return mid
                elif nums[mid] > target:
                    r = mid-1
                else :
                    l = mid+1
            return -1
        for ele in mat :
            res = search(ele , target)
            if res!= -1 :
                return 1
        return 0
            
