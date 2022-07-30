# 백준 1159번 농구 경기
# BRONZE 2
# 알고리즘 분류 : 문자열, 구현
N = int(input())
li = []
for i in range(N) :
    li.append(input()[0])
s = list(set(li))
s.sort()
ans = ''
for i in s :
    if li.count(i) >= 5 :
        ans += i
print(ans if ans else "PREDAJA")