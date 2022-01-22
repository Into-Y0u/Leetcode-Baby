class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort()
        i = 1 
        while i < len(arr):
            if arr[i-1][1] >= arr[i][0] :
                if arr[i-1][1] < arr[i][1] :
                    arr[i-1][1] = arr[i][1]
                    
                del arr[i]
            else :
                i+=1
        return arr
