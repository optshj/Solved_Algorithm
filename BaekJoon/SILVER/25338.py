# 백준 25338번 바지 구매
# SILVER 4
# 알고리즘 분류 : 수학, 사칙연산
import sys
input = sys.stdin.readline
a,b,c,d = map(int,input().split())
N = int(input())
cnt = 0
li = [list(map(int,input().split())) for _ in range(N)]
for i in li :
    wide = max(a*(i[1]-b)**2+c,d)
    if i[0] == wide :
        cnt += 1
print(cnt)