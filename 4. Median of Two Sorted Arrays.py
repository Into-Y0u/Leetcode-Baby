class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        if n%2 ==  0:
            n2 = n//2 
            n1 = n2 - 1
        else :
            n2 = -1
            n1 = n//2 
        dp = [0] * ((len(nums1) + len(nums2)) + 1 )
        # print(n1,n2)
        
        i,j ,k =0, 0 , 0 
        while i< len(nums1) and j <len(nums2):
            if nums1[i] <= nums2[j]:
                dp[k] = nums1[i]
                i+=1    
            else :
                dp[k] = nums2[j]
                j+=1
            k+=1
        # print(i , j)
        while i < len(nums1) : 
            dp[k] = nums1[i]
            i+=1
            k+=1
        while j < len(nums2) :
            dp[k] = nums2[j]
            j+=1
            k+=1

        # print(dp)

        if n2 == -1 :
            return dp[n1]
        else:
            tmp = (dp[n1] + dp[n2]) / 2 
            return tmp
           
