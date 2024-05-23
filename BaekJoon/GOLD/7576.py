# 백준 7576번 토마토
# GOLD 5
# 알고리즘 분류 : 그래프 탐색, 그래프 이론, 너비 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
q = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
li = []
def bfs() :
    v = 0
    check = 1
    for i in range(M) :
        li.append(list(map(int,input().split())))
        for j in range(N) :
            if li[i][j] == 1 :
                q.append([j,i,v])
    while q :
        x,y,v = q.popleft()
        for _ in range(4) :
            x_ = x + dx[_]
            y_ = y + dy[_]
            if x_ >= 0 and x_ <= N-1 and y_ >= 0 and y_ <= M-1 and li[y_][x_] == 0 :
                li[y_][x_] = 1
                q.append([x_,y_,v+1])
    for i in li :
        if 0 in i :
            check = 0
            break
    if check :
        print(v)
    else :
        print(-1)
bfs()