N = int(input())
'''
m = sorted(list(map(int, input().split())))
print(m)

a = []
for i in range(N):
    a.append(m[i])
    for j in range(N):
      a.append(m[i] + m[j])
      a.append(sum(m[:i + 1]))

count = 0
c = list(set(a))
q = []
for i in range(len(c)):
    while c[i] > count:
        count += 1
        if c[i] != count:
            q.append(count)
print(min(q))
'''
data = sorted(list(map(int, input().split())))

target = 1

for i in data:
    if target < i:
        break
    target += i
print(target)
# 1, 1, 2, 3, 9 이면
# (target + 1 + 1) > 2 이므로 2 이하는 전부 구현 가능
# (target + 1 + 1 + 2) > 3 이므로 3 이하는 전부 구현 가능
# (target + 1 + 1 + 2 + 3) > 9 는 거짓이므로 구현 불가능


