# N = 열  M =
#숫자 카드게임
import time
start = time.time()
'''
N, M = map(int,input().split())
a = []
for i in range(N):
    list = []
    list += map(int, input().split())
    a.append(min(list))
print(max(a))
'''


"""n, m = map(int,input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)

    result = max(result, min_value)
    print(result)
    """


end = time.time()
print(end - start)
