import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    # a <- node  b <- 가는 노드 c <= edge
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def smallest_node():
    min_values = INF
    index = 0
    for i in range(n + 1):
        if distance[i] < min_values and not visited[i]:
            min_values = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]

    for j in range(n - 1):
        now = smallest_node()
        visited[now] = True
        for k in graph[now]:
            cost = distance[now] + k[1]
            if cost < distance[k[0]]:
                distance[k[0]] = cost
print(dijkstra(start))
print(distance)








# input
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
# output
[1000000000, 0, 2, 3, 1, 2, 4]

Process finished with exit code 0
