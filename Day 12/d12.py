from collections import defaultdict

class GraphNode:
    def __init__(self, id):
        self.id = id
        self.adjList = []

    def addAdjacent(self, adj):
        self.adjList.append(adj)

def countPaths(source, dest, visited, partOne = True):
    if source.id == dest.id:
        return 1
    if source.id.islower():
        if source.id != 'start':
            visited[source.id] += 1
    count = 0
    for adj in source.adjList:
        if adj.id.isupper():
                count += countPaths(adj, dest, visited, partOne)
        elif adj.id != 'start':
            if partOne:
                if visited[adj.id] < 1:
                    count += countPaths(adj, dest, visited, partOne)
            else:
                if visited[adj.id] < 1 or len(list(filter(lambda k: visited[k] >= 2, visited))) < 1:
                    count += countPaths(adj, dest, visited, partOne)
    if source.id.islower():
        if source.id != 'start':
            visited[source.id] -= 1
    return count

def partOne(partOne = True):
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        graphList = {}
        for x in lines:
            source, destination = x.strip().split('-')
            if source not in graphList:
                graphList[source] = GraphNode(source)
            curGraph = graphList[source]
            if destination not in graphList:
                graphList[destination] = GraphNode(destination)
            curDest = graphList[destination]
            curGraph.addAdjacent(graphList[destination])
            curDest.addAdjacent(graphList[source])

        return countPaths(graphList['start'], graphList['end'], defaultdict(int), partOne)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(False))
