# 백준 14442번 벽 부수구 이동하기 2
# GOLD 3
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
# +1을 안해서 TLE만 17번 낸 문제
from collections import deque
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
li = [list(map(int,input().rstrip())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs() :
    q = deque()
    q.append((0,0,0))
    check = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    check[0][0][0] = 1
    while q :
        x,y,v = q.popleft()
        if x == M-1 and y == N-1 :
            return check[y][x][v]
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < M and 0 <= y_ < N :
                if li[y_][x_] == 0 and check[y_][x_][v] == 0 :
                    check[y_][x_][v] = check[y][x][v] + 1
                    q.append((x_,y_,v))
                elif li[y_][x_] == 1 and v < K and check[y_][x_][v+1] == 0 :
                    check[y_][x_][v+1] = check[y][x][v] + 1
                    q.append((x_,y_,v+1))
    return -1
print(bfs())