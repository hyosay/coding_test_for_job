# 문자열 삽입
s = input()

# 초기값 0
count0 = 0
count1 = 0
# 0이 들어갔으면 count0 += 1, 1이 들어갔으면 count1 += 1
if s[0] == '0':
    count0 += 1
else:
    count1 += 1

# 문자열이 바뀌면 count += 1
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1
print(min(count0, count1))

