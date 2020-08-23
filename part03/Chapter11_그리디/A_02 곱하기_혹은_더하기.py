N = input()

group = sorted([int(i) for i in N])
all = 0

for i in range(0, len(group)):
    if all + group[i] < all * group[i]:
        all *= group[i]
    else:
        all += group[i]
print(all)