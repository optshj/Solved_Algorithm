#1932번 정수 삼각형
#SILVER 1
import sys
N = int(sys.stdin.readline())
li = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
for i in range(1,N) :
    m = [0]*(i+1)
    m[0] =li[i-1][0] + li[i][0]
    m[len(li[i])-1] = li[i-1][len(li[i])-2] + li[i][len(li[i])-1]
    for j in range(1,len(li[i])-1) :
        m[j] = max(li[i-1][j-1],li[i-1][j]) + li[i][j]
    li[i] = m
print(max(li[-1]))