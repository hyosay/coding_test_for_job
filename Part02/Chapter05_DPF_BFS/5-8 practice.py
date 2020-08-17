'''a = [False if i % 2 == 0 else True for i in range(10)]
f = []
t = []
print(a)
for i in range(len(a)):
    if a[i]: # True 때 삽입
        t.append(a[i])
    else:   # False 일떄 삽입
        f.append(a[i])

print(t, f)
'''

a = [i for i in range(1, 10)]
b = [False, True]

if not a: # f t
    print('거짓참',a)

if a:
    print('참참',a)

