class FreqStack:

    def __init__(self):
        self.dicu = {}
        self.max_cont = 0
        self.st = {}
        
    def push(self, val: int) -> None:
        valcnt = self.dicu.get(val,0) + 1
        self.dicu[val] = valcnt
        if valcnt > self.max_cont :
            self.max_cont  = valcnt 
            self.st[valcnt] = []
        self.st[valcnt].append(val)
        
    def pop(self) -> int:
        res = self.st[self.max_cont].pop() 
        self.dicu[res] -=  1
        if not self.st[self.max_cont]:
            self.max_cont -= 1
        
        return res
        
