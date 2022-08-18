# 백준 1600번 말이 되고싶은 원숭이
# GOLD 3
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
dx = [0,0,1,-1]
dy = [1,-1,0,0]
hx = [-2,-1,1,2,2,1,-1,-2]
hy = [1,2,2,1,-1,-2,-2,-1]

K = int(input())
W,H = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(H)]
check = [[[INF]*(K+1) for _ in range(W)] for _ in range(H)]
def bfs(x,y) :
    q = deque()
    q.append([x,y,0])
    check[y][x][0] = 0

    while q :
        x,y,v = q.popleft()
        if x == W-1 and y == H-1 :
            return check[y][x][v]
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > W-1 or y_ < 0 or y_ > H-1 :
                continue
            if li[y_][x_] != 1 and check[y_][x_][v] == INF:
                check[y_][x_][v] = check[y][x][v] + 1
                q.append([x_,y_,v])
        if v < K :
            for i in range(8) :
                x_ = x + hx[i]
                y_ = y + hy[i]
                if x_ < 0 or x_ > W-1 or y_ < 0 or y_ > H-1 :
                    continue
                if li[y_][x_] != 1 and check[y_][x_][v+1] == INF :
                    check[y_][x_][v+1] = check[y][x][v] + 1
                    q.append([x_,y_,v+1])
    
    return -1
print(bfs(0,0))