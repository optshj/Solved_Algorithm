# 백준 11404번 플로이드
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 플로이드-워셜
# 그래프를 입력받고 플로이드 알고리즘으로 최단거리를 구하면 되는 문제
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
time = [[sys.maxsize]*(n+1) for _ in range(n+1)]

for i in range(m) :
    a,b,c = map(int,input().split())
    time[a][b] = min(c,time[a][b])
for i in range(n+1) :
    time[i][i] = 0
for k in range(n+1) :
    for i in range(n+1) :
        for j in range(n+1) :
            time[i][j] = min(time[i][j],time[i][k]+time[k][j])
for i in time[1:] :
    for j in i[1:] :
        if j == sys.maxsize :
            print(0,end = ' ')
        else :
            print(j,end = ' ')
    print()