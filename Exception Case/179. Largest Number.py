class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        
        def compare(n1,n2):
            if n1 + n2 > n2 + n1 :
                return -1
            else :
                return 1
            
        nums = sorted(nums , key = cmp_to_key(compare))          # cmp_key_to(function) to compare each and every element side by side of nums
        
        return str(int(str("".join(nums))))
        
