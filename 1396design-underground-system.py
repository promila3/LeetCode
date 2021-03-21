#https://leetcode.com/problems/design-underground-system/
class UndergroundSystem:

    def __init__(self):
        self.customer = {} # station name and check in time
        self.stations = {} # start station, end station, trip times
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station = self.customer[id][0]
        if start_station not in self.stations:
            self.stations[start_station] = {}
        if stationName not in self.stations[start_station]:
            self.stations[start_station][stationName] = []
        self.stations[start_station][stationName].append(t - self.customer[id][1])
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if not self.stations[startStation]:
            return 0
        if not self.stations[startStation][endStation]:
            return 0
        n = len(self.stations[startStation][endStation])
        total = sum(self.stations[startStation][endStation]) * 1.0
        result, temp = divmod(total, n)
        return total / n


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
