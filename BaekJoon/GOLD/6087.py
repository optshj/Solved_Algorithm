# 백준 6087번 레이저 통신
# GOLD 3
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 데이크스트라
# 방향을 안바꾸는 경우를 우선적으로 탐색 appendleft 이용
import sys
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs() :
    q = deque()
    ans = 1e9
    for i in range(4) :
        q.append([sx,sy,i,0])
        check[sy][sx][i] = 1
    while q :
        x,y,t,v = q.popleft()
        check[y][x][t] = 1
        if x == ax and y == ay :
            return v
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > W-1 or y_ < 0 or y_ > H-1 :
                continue
            if li[y_][x_] != '*' and not check[y_][x_][i] :
                if i == t :
                    q.appendleft([x_,y_,i,v])
                else :
                    q.append([x_,y_,i,v+1])
W,H = map(int,input().split())
li = [list(input()) for _ in range(H)]
check = [[[0]*4 for _ in range(W)] for _ in range(H)]
flag = 0
for i in range(H) :
    for j in range(W) :
        if li[i][j] == 'C' :
            if flag == 0 :
                sx,sy = j,i
                flag = 1
            else :
                ax,ay = j,i
print(bfs())