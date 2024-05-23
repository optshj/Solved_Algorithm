# 백준 11559번 Puyo Puyo
# GOLD 4
# 알고리즘 분류 : 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션
from collections import deque
li = [list(input()) for _ in range(12)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0

def bfs(x,y,c) :
    val = []
    q = deque()
    q.append([x,y])
    val.append([x,y])
    check[y][x] = 1
    while q :
        x,y = q.popleft()
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > 5 or y_ < 0 or y_ > 11 :
                continue
            if li[y_][x_] == c and not check[y_][x_] :
                q.append([x_,y_])
                val.append([x_,y_])
                check[y_][x_] = 1
    if len(val) > 3 :
        return val
    return []

def move() :
    val.sort()
    for x,y in val :
        li[y][x] = '.'
    for x,y in val :
        for k in range(y-1,-1,-1) :
            li[k+1][x] = li[k][x]
        li[0][x] = '.'

while True :
    flag = 0
    check = [[0]*6 for _ in range(12)]
    val = []
    for i in range(11,-1,-1) :
        for j in range(6) :
            if li[i][j] != '.' :
                k = bfs(j,i,li[i][j])
                if k :
                    val += k
                    flag = 1
    if flag :
        ans += 1
    move()
    if not flag :
        break 
print(ans)