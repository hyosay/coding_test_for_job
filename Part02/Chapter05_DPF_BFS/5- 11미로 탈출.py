from collections import deque
# n, m값을 입력
n, m = map(int, input().split())
# 미로 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌 ,우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 구현
'''def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque() 사용
    queue = deque()
    queue.append((x, y))
    # queue가 빌 때까지 반복
    while queue:
        print(graph)
        x, y = queue.popleft()
        # 현재 위치에서 네 방향을 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 무시한 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는 부분(벽이 있는 부분)
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 겨리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 마지막까지의 최단 거리 반환
    return graph[n - 1][m - 1]'''
# 수행 결과


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))
    return graph[n- 1][m - 1]
print(bfs(0, 0))



