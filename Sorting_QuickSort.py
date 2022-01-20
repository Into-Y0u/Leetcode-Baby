import sys
class Solution:  
    def sortArray(self, arr: List[int]) -> List[int]:
        # arr.append(sys.maxsize)
        l,h = 0, len(arr)-1
        def quicksort(l,h):
            if l < h :
                j = partition(l,h)
                quicksort(l,j-1)
                quicksort(j+1,h)
            
        def partition(l,h) :
            piv_ind = l
            pivot = arr[l]
            while l < h :
                while l < len(arr) and arr[l] <= pivot :
                    l+=1
                while arr[h] > pivot :
                    h-=1
                if l < h :
                    arr[l],arr[h] =  arr[h],arr[l]
            arr[piv_ind],arr[h] = arr[h] , arr[piv_ind] 
            return h
        quicksort(l,h)
        return arr
    



        
