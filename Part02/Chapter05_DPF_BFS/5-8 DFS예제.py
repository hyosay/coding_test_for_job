'''def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    print(visited)
    visited[v] = True
    print(v, end= ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)
'''
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
'''
visited = [False] * 9

dfs(graph,1, visited)
'''



'''

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for i in graph[v]:
        if not i in discovered:
            discovered = recursive_dfs(i, discovered)
    return discovered

print(recursive_dfs(1))


'''
def dfs(v):
   visited[v] = 1
   print(v, end=' ')

   for i in graph[v]:
       if not visited[i]:
           dfs(i)



n = int(input())
visited = [0] * 10
dfs(n)