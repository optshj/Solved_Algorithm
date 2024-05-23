# 백준 2589번 보물섬
# GOLD 5
# 알고리즘 분류 : 그래프, 브루트포스 알고리즘
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
li = [input() for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y) :
    res = [[0]*M for _ in range(N)]
    q = deque()
    q.append([x,y,0])
    res[y][x] = 1
    while q :
        x,y,v = q.popleft()
        for k in range(4) :
            x_ = x + dx[k]
            y_ = y + dy[k]
            v_ = v + 1
            if x_ < 0 or x_ > M-1 or y_ < 0 or y_ > N-1  :
                continue
            if res[y_][x_] == 0 and li[y_][x_] == 'L' :
                q.append([x_,y_,v_])
                res[y_][x_] = 1
    return v_ - 1
ans = 0
for i in range(M) :
    for j in range(N) :
        if li[j][i] == 'L' :
            ans = max(ans,bfs(i,j))
print(ans)