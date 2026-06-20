def dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    
    visited.add(start)
    result.append(start)
    
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, result)
    
    return result

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print(dfs(graph, 'A'))  