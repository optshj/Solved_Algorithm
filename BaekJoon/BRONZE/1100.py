# 백준 1100번 하얀 칸
# BRONZE 1
# 알고리즘 분류 : 구현, 문자열
li = [list(input()) for _ in range(8)]
cnt = 0
for i in range(8) :
    for j in range(8) :
        if li[i][j] == 'F' and (i+j)%2 == 0:
            cnt += 1
print(cnt)