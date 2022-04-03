class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        n = len(arr)
        i = n-1 ; f = 0
        while i> 0 :
            if arr[i] > arr[i-1] :
                f = 1
                break
            i-=1
        # print(f)
        if f :
            
            # lowest of part 2 array swapping with break point target
            for j in range(n-1,i-2,-1):
                if arr[j] > arr[i-1] :
                    arr[i-1] , arr[j] = arr[j] , arr[i-1]
                    break
            l = n-1
            j = i
            
            # simple sorting the rest array
            while j < l :
                arr[j],arr[l] = arr[l] , arr[j]
                l-=1
                j+=1
                

            return arr
        else :
            arr.reverse()
            return arr
