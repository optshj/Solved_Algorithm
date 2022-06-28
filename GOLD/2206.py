# 백준 2206번 벽 부수고 이동하기
# GOLD 4
# 알고리즘 분류 : 그래프
# 벽을 부쉈는지 안부쉈는지를 3차원 배열을 이용해 확인하면서 최단경로 탐색을 진행함
from collections import deque
N,M = map(int,input().split())
li = [list(input()) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs() :
    res = [[[0]*2 for _ in range(M)] for _ in range(N)]
    res[0][0][0] = 1
    q = deque()
    q.append([0,0,0])
    while q :
        x,y,w = q.popleft()
        if x == M-1 and y == N-1 :
            return res[-1][-1][w]
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > M-1 or y_ < 0 or y_ > N-1 :
                continue
            if li[y_][x_] == '0' and res[y_][x_][w] == 0 :
                res[y_][x_][w] = res[y][x][w] + 1
                q.append([x_,y_,w])
            if li[y_][x_] == '1' and w == 0 :
                res[y_][x_][1] = res[y][x][w] + 1
                q.append([x_,y_,1])
    return -1
print(bfs())