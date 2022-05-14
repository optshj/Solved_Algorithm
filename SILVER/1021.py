#1021번 회전하는 큐
#SILVER 4
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
li = list(map(int,input().split()))
k = list(range(1,N+1))
cnt = 0
now = 0
for i in li :
    j = k.index(i)
    cnt += min(abs(now - j),abs(N-j+now),abs(N-now+j))
    now = j
    k.pop(j)
    N -= 1
print(cnt)