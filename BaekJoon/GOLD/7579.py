# 백준 7579번 토마토
# GOLD 5
# 알고리즘 분류 : 그래프 탐색, 그래프 이론, 너비 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline
M,N,H = map(int,input().split())
q = deque()
dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]
li = []
def bfs() :
    v = 0
    check = 1
    for i in range(H) :
        li.append([list(map(int,input().split())) for _ in range(N)])
        for j in range(M) :
            for m in range(N) :
                if li[i][m][j] == 1 :
                    q.append([i,m,j,v])
    while q :
        z,x,y,v = q.popleft()
        for _ in range(6) :
            x_ = x + dx[_]
            y_ = y + dy[_]
            z_ = z + dz[_]
            if x_ >= 0 and x_ <= N-1 and y_ >= 0 and y_ <= M-1 and z_>= 0 and z_ <= H-1 and li[z_][x_][y_] == 0 :
                li[z_][x_][y_] = 1
                q.append([z_,x_,y_,v+1])
    for i in range(H) :
        for j in li[i] :
            if 0 in j :
                check = 0
                break
    if check :
        print(v)
    else :
        print(-1)
bfs()