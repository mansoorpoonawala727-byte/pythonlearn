from collections import deque

def bfs(graph, start):
    visited = set()     
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    
    return result

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print(bfs(graph, 'A'))  