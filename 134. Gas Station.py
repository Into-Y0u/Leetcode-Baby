class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0 ; extra = 0 ; cur =  0
        for i in range(len(gas)) :
            cur += gas[i] - cost[i]
            if cur < 0 :
                extra += cur 
                start = i + 1
                cur = 0
        return start if (cur + extra) >= 0 else -1
        
