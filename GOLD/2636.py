# 백준 2636번 치즈
# GOLD 4
# 알고리즘 분류 : 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션
from collections import deque
from copy import deepcopy
import sys
dx = [1,-1,0,0]
dy = [0,0,1,-1]
input = sys.stdin.readline
N,M = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
def count() :
    cnt = 0
    for i in range(N) :
        for j in range(M) :
            if li[i][j] :
                cnt += 1
    return cnt
    
def bfs(x,y) :
    q = deque()
    q.append([x,y])
    check[y][x] = 1
    while q :
        x,y = q.popleft()
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > M-1 or y_ < 0 or y_ > N-1 or check[y_][x_] :
                continue
            if li[y_][x_] == 1 :
                map[y_][x_] = 0
                check[y_][x_] = 1
            else :
                q.append([x_,y_])
                check[y_][x_] = 1

ans = 0
cnt = count()
while True :
    before = cnt
    map = deepcopy(li)
    check = [[0]*M for _ in range(N)]
    for i in range(M) :
        if li[0][i] == 0 and not check[0][i] :
            bfs(i,0)
        if li[N-1][i] == 0 and not check[N-1][i] :
            bfs(i,N-1)
    for j in range(N) :
        if li[j][0] == 0 and not check[j][0] :
            bfs(0,j) 
        if li[j][M-1] == 0 and not check[j][M-1] :
            bfs(M-1,j)
    li = deepcopy(map)
    cnt = count()
    ans += 1
    if cnt == 0 :
        break
    
print(ans)
print(before)