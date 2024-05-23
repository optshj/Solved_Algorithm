# 백준 1175번 배달
# GOLD 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
# 비트마스킹처럼 어떤 C를 방문했는지 표시함.
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs() :
    q = deque()
    for i in range(4) :
        q.append([sx,sy,0,i,0])
        check[sy][sx][i][0] = 1
    while q :
        x,y,v,c,l = q.popleft()
        if li[y][x] == 'C' :
            if x == fcx and y == fcy :
                if l != 1 :
                    l += 1
            else :
                if l != 2 :
                    l += 2
            if l == 3 :
                return v
        for i in range(4) :
            if i == c :
                continue
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > M-1 or y_ < 0 or y_ > N-1 :
                continue
            if check[y_][x_][i][l] : 
                continue
            if li[y_][x_] == '.' or li[y_][x_] == 'C' :
                check[y_][x_][i][l] = 1
                q.append([x_,y_,v+1,i,l])
    return -1

N,M = map(int,input().split())
li = [list(input()) for _ in range(N)]
check = [[[[0]*4 for _ in range(4)] for _ in range(M)] for _ in range(N)]
for i in range(N) :
    for j in range(M) :
        if li[i][j] == 'S' :
            li[i][j] = '.'
            sx,sy = j,i
        if li[i][j] == 'C' :
            fcx,fcy = j,i
print(bfs())