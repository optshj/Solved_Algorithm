# 백준 2178번 미로 탐색
# SILVER 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
from collections import deque
N,M = map(int,input().split())
li = [list(map(int,input())) for _ in range(N)]
k = deque()
m = [[-1,0],[1,0],[0,-1],[0,1]]
def bfs(x,y) :
    global cnt
    k.append((x,y))
    while k :
        x,y = k.popleft()
        for _ in range(4) :
            x_ = x + m[_][0]
            y_ = y + m[_][1]
            if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > M-1 :
                continue
            if li[x_][y_] == 1 :
                li[x_][y_] = li[x][y] + 1
                k.append((x_,y_))
bfs(0,0)
print(li[N-1][M-1])