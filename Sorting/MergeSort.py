class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr) > 1 :
            mid = len(arr)//2 
            l = arr[:mid]
            r = arr[mid:]
            self.sortArray(l)
            self.sortArray(r)
            
            i,j,k = 0, 0 , 0
            while i < len(l) and j < len(r) :
                if l[i] <= r[j] :
                    arr[k] = l[i]
                    i+=1
                else :
                    arr[k] = r[j]
                    j+=1
                k+=1
                    
            while i < len(l) :
                arr[k] = l[i]
                i+=1
                k+=1
             
            while  j < len(r) :
                arr[k] = r[j]
                j+=1
                k+=1
            return arr
        else :
            return arr
            

        
