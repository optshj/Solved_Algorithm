# 백준 16952번 체스판 여행 2
# PLATINUM 5
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 플로이드-워셜
# 이전에 탐색한 경우보다 말을 바꾼 횟수가 작은 경우에만 탐색한다.
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
check = [[[[1e9]*3 for _ in range(N**2+1)] for _ in range(N)] for _ in range(N)]
def bfs() :
    ans = 1e9
    change = 1e9
    while q :
        x,y,n,c,v,cnt = q.popleft()
        if n == N**2 :
            if v < ans :
                ans = v
                change = cnt
            elif v == ans :
                if change > cnt :
                    change = cnt
        for i in range(3) :
            if i == c :
                continue
            if check[y][x][n][i] <= cnt + 1 :
                continue
            check[y][x][n][i] = cnt + 1
            q.append([x,y,n,i,v+1,cnt+1])
        # 나이트
        if c == 0 :
            for i in range(8) :
                x_ = x + kx[i]
                y_ = y + ky[i]
                if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
                    continue
                if li[y_][x_] == n + 1 :
                    if check[y_][x_][n+1][c] <= cnt :
                        continue
                    check[y_][x_][n+1][c] = cnt
                    q.append([x_,y_,n+1,c,v+1,cnt])
                else :
                    if check[y_][x_][n][c] <= cnt :
                        continue
                    check[y_][x_][n][c] = cnt
                    q.append([x_,y_,n,c,v+1,cnt])

        # 비숍
        elif c == 1 :
            for i in range(4) :
                x_ = x
                y_ = y
                while True :
                    x_ += bx[i]
                    y_ += by[i]
                    if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
                        break
                    if li[y_][x_] == n + 1 :
                        if check[y_][x_][n+1][c] <= cnt :
                            continue
                        check[y_][x_][n+1][c] = cnt
                        q.append([x_,y_,n+1,c,v+1,cnt])
                    else :
                        if check[y_][x_][n][c] <= cnt :
                            continue
                        check[y_][x_][n][c] = cnt
                        q.append([x_,y_,n,c,v+1,cnt])

        # 룩
        else :
            for i in range(4) :
                x_ = x
                y_ = y
                while True :
                    x_ += lx[i]
                    y_ += ly[i]
                    if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
                        break
                    if li[y_][x_] == n + 1 :
                        if check[y_][x_][n+1][c] <= cnt :
                            continue
                        check[y_][x_][n+1][c] = cnt
                        q.append([x_,y_,n+1,c,v+1,cnt])
                    else :
                        if check[y_][x_][n][c] <= cnt :
                            continue
                        check[y_][x_][n][c] = cnt
                        q.append([x_,y_,n,c,v+1,cnt])
    return ans,change
for i in range(N) :
    for j in range(N) :
        if li[i][j] == 1 :
            for k in range(3) :
                check[i][j][1][k] = 0
                q.append([j,i,1,k,0,0])
time,cnt = bfs()
print(time,cnt)