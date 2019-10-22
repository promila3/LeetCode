# TimeOut in Large input case
# https://leetcode.com/submissions/detail/272081981/
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        # create adjacency list that would make it easier. 
        adjList = {}
        for edge in paths:
            if edge[0] in adjList.keys():
                if edge[1] in adjList[edge[0]] :
                    pass
                else:
                    adjList[edge[0]].append(edge[1])
            else:
                adjList[edge[0]] = [edge[1]]
            if edge[1] in adjList.keys():
                if edge[0] in adjList[edge[1]] :
                    pass
                else:
                    adjList[edge[1]].append(edge[0])
            else:
                adjList[edge[1]] = [edge[0]]
                
        queue = []
        listNodes = [ x for x in range(1, N+1)]
        colorG = {}
        while len(listNodes) != 0:
            queue.append(listNodes[0])
            listNodes.remove(listNodes[0])
            
            while len(queue) != 0:
                currentG = queue.pop(0)
                
                if currentG not in colorG.keys():
                    notColor =[]
                    if currentG in adjList.keys():
                        for node in adjList[currentG]:
                            if node in colorG.keys():
                                notColor.append(colorG[node])
                            else:
                                queue.append(node)
                            #print(node, listNodes)
                            # pop with the give value. 
                                if node in listNodes:
                                    listNodes.remove(node)
                                continue
                    colors = [1,2,3,4]
                    for color in colors:
                        if color not in notColor:
                            colorG[currentG] = color
                            break
                
        sorted(colorG)
        # Print the sorted key value pairs of dictionary using list comprehension
        result = [ value for (key, value) in sorted(colorG.items()) ]
        return result
