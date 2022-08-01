from collections import defaultdict

def addEdge(u, v):
    graph[u].append(v)

def dfs(start, goal, depth):
    print(start, end = " ")
    if start == goal:
        return True
    if depth <= 0:
        return False
    for i in graph[start]:
        if dfs(i, goal, depth - 1):
            return True
    return False
    

def dfid(start, goal, maxDepth):
    print(f"DFID for start node {start}, goal node {goal}")
    for i in range(maxDepth):
        print("\nDFS at level", i + 1)
        print("Path taken:", end = " ")
        isPathFound = dfs(start, goal, i)
        if isPathFound:
            print("\nGoal node  found")
            return
        else:
            print("\nGoal node not found")
    

graph = defaultdict(list)
addEdge('A', 'B')
addEdge('A', 'C')
addEdge('B', 'D')
addEdge('B', 'E')
addEdge('C', 'F')
addEdge('C', 'G')
dfid('A', 'Z', 3)
