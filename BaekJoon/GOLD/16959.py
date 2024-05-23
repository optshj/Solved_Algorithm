# 백준 16959번 체스판 여행 1
# GOLD 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
from collections import deque
kx = [2,1,-1,-2,-2,-1,1,2]
ky = [1,2,2,1,-1,-2,-2,-1]
bx = [1,1,-1,-1]
by = [-1,1,1,-1]
lx = [1,-1,0,0]
ly = [0,0,1,-1]
N = int(input())
li = [list(map(int,input().split()))for _ in range(N)]
q = deque()
check = [[[[0]*3 for _ in range(N**2+1)] for _ in range(N)] for _ in range(N)]
def bfs() :
    ans = 1e9
    while q :
        x,y,n,c,v = q.popleft()
        if n == N**2 :
            ans = min(ans,v)
        for i in range(3) :
            if i == c :
                continue
            if not check[y][x][n][i] :
                check[y][x][n][i] = 1
                q.append([x,y,n,i,v+1])
        # 나이트
        if c == 0 :
            for i in range(8) :
                x_ = x + kx[i]
                y_ = y + ky[i]
                if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
                    continue
                if li[y_][x_] == n + 1 and not check[y_][x_][n+1][c] :
                    check[y_][x_][n+1][c] = 1
                    q.append([x_,y_,n+1,c,v+1])

                if not check[y_][x_][n][c] :
                    check[y_][x_][n][c] = 1
                    q.append([x_,y_,n,c,v+1])

        # 비숍
        elif c == 1 :
            for i in range(4) :
                k = 0
                while True :
                    x_ = x + bx[i]*k
                    y_ = y + by[i]*k
                    if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
                        break
                    if li[y_][x_] == n + 1 and not check[y_][x_][n+1][c] :
                        check[y_][x_][n+1][c] = 1
                        q.append([x_,y_,n+1,c,v+1])

                    if not check[y_][x_][n][c] :
                        check[y_][x_][n][c] = 1
                        q.append([x_,y_,n,c,v+1])
                    k += 1

        # 룩
        else :
            for i in range(4) :
                k = 0
                while True :
                    x_ = x + lx[i]*k
                    y_ = y + ly[i]*k
                    if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
                        break
                    if li[y_][x_] == n + 1 and not check[y_][x_][n+1][c] :
                        check[y_][x_][n+1][c] = 1
                        q.append([x_,y_,n+1,c,v+1])

                    if not check[y_][x_][n][c] :
                        check[y_][x_][n][c] = 1
                        q.append([x_,y_,n,c,v+1])
                    k += 1
    return ans
for i in range(N) :
    for j in range(N) :
        if li[i][j] == 1 :
            for k in range(3) :
                check[i][j][1][k] = 1
                q.append([j,i,1,k,0])
print(bfs())