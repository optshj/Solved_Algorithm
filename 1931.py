#1931번 회의실 배정
#SILVER 1
import sys


input = sys.stdin.readline
N = int(input())
li = []
cnt = 0
for _ in range(N):
    li.append(list(map(int,input().split())))
li.sort(key = lambda x:(x[1],x[0]))
end = 0
for i in range(N):
    if end <= li[i][0]:
        cnt += 1
        end = li[i][1]
print(cnt)