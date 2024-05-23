# 백준 5525번 IOIOI
# SILVER 1
# 알고리즘 분류 : 문자열
N = int(input())
M = int(input())
li = input()
cnt = 0
ans = 0
i = 1
while (i < M-1) :
    if li[i-1] == 'I' and li[i] == 'O' and li[i+1] == 'I' :
        cnt += 1
        if cnt == N :
            ans += 1
            cnt -= 1
        i += 1
    else :
        cnt = 0
    i += 1
print(ans)