class Solution:
	def hasZeroSumSubarray(self, nums: List[int]) -> bool:
		vis = set()
		x = 0
		for n in nums :
			x+=n 
			if x==0 or x in vis :
				return 1 
			vis.add(x)
		return 0
