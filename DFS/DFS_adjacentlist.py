def dfs(graph, start_node):
  visited = []
  stack = []
  stack.append(start_noede)
  
  while stack:
    node = stack.pop()
    if node not in visited:
      visited.append(node)
      stack.extend(graph[node]
  return visited
