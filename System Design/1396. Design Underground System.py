class Node:
    def __init__(self,st_in,t):
        self.st_in = st_in
        self.time_in = t

class UndergroundSystem:

    def __init__(self):
        self.passg = dict()
        self.travel = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passg[id] = Node(stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time  = t - self.passg[id].time_in
        if self.travel.get(self.passg[id].st_in + " " + stationName) :
            self.travel[self.passg[id].st_in + " " + stationName ].append(time)
        else :
            self.travel[self.passg[id].st_in + " " + stationName ] = [time]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.travel[startStation + " " + endStation]) / len(self.travel[startStation + " " + endStation])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
