#node, edge, start node
n, m, v = map(int, input().split())
#2차원 행렬
matrix [[0] * (n + 1) for i in range(n + 1)]
# 간선의 개수만큼 matrix에 입력
for i in range(m):
  a, b = map(int, input().split())
  #양방향이기 때문에 두번 참조
  matrix[a][b] = 1
  maptrix[b][a] = 1
 
 # 방문 list
 visit_list = [0] * (n + 1)
 
 # dfs 구현
 def dfs(v):
  visit_list[v] = 1
  print(v, end= ' ')
  for i in range(1, n + 1):
    if not visit_list[i] and matrix[v][i] = 1:
      dfs(i)
dfs(v)
    
 
