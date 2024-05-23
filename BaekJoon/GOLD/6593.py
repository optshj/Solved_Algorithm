# 백준 6593번 상범 빌딩
import sys
from collections import deque
input = sys.stdin.readline
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
def bfs() :
    while q :
        x,y,z = q.popleft()
        for i in range(6) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            z_ = z + dz[i]
            if x_ < 0 or x_ > C-1 or y_ < 0 or y_ > R-1 or z_ < 0 or z_ > L-1 :
                continue
            if li[z_][y_][x_] == 'E' :
                return check[z][y][x] + 1
            if li[z_][y_][x_] == '.' and not check[z_][y_][x_] :
                check[z_][y_][x_] = check[z][y][x] + 1
                q.append([x_,y_,z_])
    return 0
while True :
    L,R,C = map(int,input().split())
    if L+R+C == 0 :
        break
    li = []
    check = [[[0]*C for _ in range(R)] for _ in range(L)]
    q = deque()
    for i in range(L) :
        li.append([list(input().rstrip()) for _ in range(R)])
        input()
    for i in range(L) :
        for j in range(R) :
            for k in range(C) :
                if li[i][j][k] == 'S' :
                    q.append([k,j,i])
                if li[i][j][k] == 'E' :
                    sx,sy,sz = k,j,i
    val = bfs()
    if val :
        print(f"Escaped in {val} minute(s).")
    else :
        print("Trapped!")