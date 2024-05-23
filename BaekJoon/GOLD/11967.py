# 백준 11967번 불켜기
# GOLD 2
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
from collections import deque
import sys
dx = [1,-1,0,0]
dy = [0,0,1,-1]
N,M = map(int,input().split())
light = [[0]*N for _ in range(N)]
visit = [[0]*N for _ in range(N)]
light[0][0] = 1
g = [[[] for _ in range(N)] for _ in range(N)]
ans = 0
def bfs() :
    q = deque()
    q.append([0,0])
    visit[0][0] = 1
    while q :
        x,y = q.popleft()
        for n,m in g[y][x] :
            if not light[n][m] :
                light[n][m] = 1
                for i in range(4) :
                    x_ = m + dx[i]
                    y_ = n + dy[i]
                    if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
                        continue
                    # 불을 킨 곳 주변에 방문한 적이 있다면 주변에도 불이 켜져 있어서 방문이 가능함.
                    # 따라서 불을 킨 곳에도 방문이 가능함
                    if visit[y_][x_] :
                        q.append([m,n])
                        visit[n][m] = 1
                        break
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
                continue
            if light[y_][x_] and not visit[y_][x_] :
                q.append([x_,y_])
                visit[y_][x_] = 1
    return False
for i in range(M) :
    x,y,a,b = map(int,input().split())
    g[x-1][y-1].append([a-1,b-1])
bfs()
for i in range(N) :
    for j in range(N) :
        if light[i][j] :
            ans += 1
print(ans)