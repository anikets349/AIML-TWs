from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def DFSRec(self, s, visited):
        visited.append(s)
        print(s, end = " ")
        for i in self.graph[s]:
            if i not in visited:
                self.DFSRec(i, visited)
    def DFS(self, s):
        visited = []
        visited.append(s)
        print(s, end = " ")
        for i in self.graph[s]:
            if i not in visited:
                self.DFSRec(i, visited)
                    
g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('A', 'D')
g.addEdge('B', 'E')
g.addEdge('B', 'F')
g.addEdge('C', 'G')
g.addEdge('C', 'I')
g.addEdge('D', 'I')

print('DFS with starting node A : ', end= " ")
g.DFS('A')