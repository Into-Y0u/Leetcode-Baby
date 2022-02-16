class Solution:
    def nextday(self,cells):
        prev = cells[0]
        for i in range(1,len(cells)-1):
            p = cells[i]
            cells[i] = 1 if prev  == cells[i+1] else 0
            prev = p
        cells[0] = cells[7] =  0
        return cells
    
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = []
        for i in range(n):
            cells = self.nextday(cells)
            if cells in seen:
                ind = seen.index(cells)
                cycle  = abs(i - ind)
                cropped = (n-i)%cycle
                arr = seen[ind:]
                return arr[cropped-1]

            else :
                seen.append(cells[:])
                n-=1
        return cells
                
