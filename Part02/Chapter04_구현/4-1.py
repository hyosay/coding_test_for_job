N = int(input())
x, y = 1 , 1
move =  input().split()
print(move)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
logue = ['L', 'R', 'U', 'D']

for i in move:
    for j in range(len(logue)):
        if i == logue[j]:
            nx = dx[j] + x
            ny = dy[j] + y
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny
print(x, y)
