class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%(len(nums))
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
