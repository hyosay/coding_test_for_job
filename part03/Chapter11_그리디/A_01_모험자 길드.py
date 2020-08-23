member = int(input())

fear_level = list(map(int, input().split()))

fear_level.sort()
'''

group = 0
count = 0
for i in fear_level:
    count += 1
    if count >= i:
        group += 1
        count = 0
print(group)
'''

count = 0
result = 0
for i in fear_level:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)

