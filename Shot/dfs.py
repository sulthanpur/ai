from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend([n for n in graph[vertex] if n not in visited])

graph = {
   'A' : ['B','C'],
'B' : ['A','C','D'],
'C' : ['A','B','E'],
'D' : ['B','E'],
'E' : ['C','D']
}
bfs(graph, 'A')