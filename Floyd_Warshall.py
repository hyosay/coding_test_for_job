# 최단 거리 플로이드 워셜
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1)for i in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0
for i in  range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print('IFK', end= ' ')
        else:
            print(graph[i][j], end= ' ')
    print()




4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
