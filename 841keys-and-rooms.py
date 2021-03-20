#841 https://leetcode.com/problems/keys-and-rooms/
class Solution:
    def canVisitAllRooms1(self, rooms: List[List[int]]) -> bool:
        q = []
        visited = []
        
        N = len(rooms)
        if N == 0 or N == 1:
            return True
        all = [ x for x in range(N)]
        q.extend(rooms[0])
        visited.append(0)
        while len(q) > 0:
            print(q, visited)
            room = q.pop()
            if room not in visited:
                visited.append(room)
                q.extend(rooms[room])
        if len(visited) == N:
            return True
        return False
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        unlocked = [0]
        while unlocked:
            nextRoom = unlocked.pop()
            visited.add(nextRoom)
            keys = rooms[nextRoom]
            unlocked += [ key for key in keys if key not in visited ]
        return len(visited) == len(rooms)
