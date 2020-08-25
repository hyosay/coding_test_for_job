def solution(food_times, k):
    answer = 0
    return answer

N = int(input())

food_times = list(map(int, input().split()))

k = int(input())
time = sum(food_times)
for i in range(sum(food_times)):
    i  %= N
    time -= 1
    food_times[i] -= 1
    if food_times[i] == 0:


