'''n = int(input())
count = 0
list = [500, 100, 50, 10]

for coin in list:
    count = n // coin
    n %= coin


print(count)'''
n = int(input())
count = 0
list = [500, 400, 100]

for coin in list:
    count += n // coin
    n %= coin
print(count)
