# 백준 1543번 문서 검색
# SILVER 4
# 알고리즘 분류 : 문자열, 그리디 알고리즘, 브루트포스 알고리즘
a = input()
b = input()
cnt = 0
i = 0
while i <= len(a) - len(b) :
    if a[i:i+len(b)] == b :
        i += len(b)
        cnt += 1
    else :
        i += 1
print(cnt)