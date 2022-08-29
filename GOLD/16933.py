# 백준 16933번 벽 부수고 이동하기 3
# GOLD 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
# 함수에 넣고 돌리면 TLE가 났음. 기묘한 언어 파이썬
from collections import deque
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
li = [list(input().rstrip()) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque()
q.append((0,0,0,0))
check = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
check[0][0][0] = 1
while q :
    x,y,v,d = q.popleft()
    if x == M-1 and y == N-1 :
        print(d+1)
        exit()
    for i in range(4) :
        x_ = x + dx[i]
        y_ = y + dy[i]
        if x_ < 0 or x_ > M-1 or y_ < 0 or y_ > N-1 :
            continue
        if li[y_][x_] == '0' and check[y_][x_][v] == 0 :
            check[y_][x_][v] = d+1
            q.append((x_,y_,v,d+1))
        elif li[y_][x_] == '1' and v < K :
            if check[y_][x_][v+1] :
                continue
            if d%2 == 0 :
                check[y_][x_][v+1] = d+1
                q.append((x_,y_,v+1,d+1))
            else :
                q.append((x,y,v,d+1))
print(-1)