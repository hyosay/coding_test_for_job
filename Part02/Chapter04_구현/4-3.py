'''input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

print(row,column)
steps = [
    (2,1), (2, -1), (-2, 1), (-2, -1), (1, 2),
    (1, -2), (-1, 2),(-1, -2)
]
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1and next_column <= 8:
        result += 1
print(result)
'''


#나의 알고리즘

#좌표를 설정
input_data = input()
row = int(input_data[1])
#열은 알파벳을 8개를 배열에 넣어서 정수로 반환
col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
column = col.index(input_data[0]) + 1
#횟수
count = 0
#경우의 수를 성정(나이트의 이동방향)
step = [
    (1, 2),(1, -2), (-1, 2), (-1, -2),
    (2, 1), (-2, 1), (2, -1), (-2, -1)
]

#next_row, next_column는 이동 후 좌표
for i in step:
    next_row = row + i[0]
    next_column = column + i[1]
#이동 후 좌표(next_row, next_column)이 인덱스 아웃이 아니면 count + 1
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1
#결과값
print(count)



