import time
a = time.time()
N, K = map(int,input().split())
count = 0
while True:
    if N == 1:
        break
    elif N % K != 0:
        N -= 1
        count += 1
    elif N % K == 0:
        N = N // K
        count += 1
b = time.time()
print(b - a)
print(count)
print(N)

