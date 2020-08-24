
#N과 M을 입력
N, M = map(int, input().split())
# 공의 무게를 입력
kg = list((map(int, input().split())))

#code_1
a = []
# 2중 반복문을 이용해서 공의 무게가 같은 것을 제외하고 전부 리스트 a 에 입력
for i in range(N):
    for j in range(i + 1, N):
        if kg[i] != kg[j]:
            a.append((i + 1, j+ 1))
# a의 숫자를 셈
print(len(a))

#code_2
'''

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

# 각 무게에 대한 볼링공의 개수 카운트
for x in kg:
    array[x] += 1

result = 0
# 1 부터 M까지의 각 무게에 대하여 처리
for i in range(1, M + 1):
    N -= array[i]
    result += array[i] * N
print(result)
'''