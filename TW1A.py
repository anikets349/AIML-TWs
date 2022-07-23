from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def DFS(self, s, g, depth):
        print(s, end = " ")
        if s == g:
            return True
        if depth <= 0:
            return False
        for i in self.graph[s]:
            if self.DFS(i, g, depth - 1):
                return True
        return False
    def DFID(self, s, g, maxDepth):
        for i in range(maxDepth):
            print("DFS at level ", i)
            isPathFound = self.DFS(s, g, i)
            print("")
            if isPathFound == True:
                print("Path exists")
                return
            print("Path does not exist")
                
g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('C', 'F')
g.addEdge('C', 'G')
g.DFID('A', 'G', 3)

