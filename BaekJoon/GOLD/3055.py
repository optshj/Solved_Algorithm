# 백준 3055번 탈출
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
# check 배열에 해당 위치에 뭐가 있는지 저장하는 문제
# 물인 경우를 먼저 탐색하고 이후 고슴도치에 경우를 탐색한다.
import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
R,C = map(int,input().split())
li = [list(input().rstrip()) for _ in range(R)]
check = [[0]*C for _ in range(R)]
q = deque()
for i in range(R) :
    for j in range(C) :
        if li[i][j] == "X" :
            check[i][j] = 2
        if li[i][j] == "D" :
            check[i][j] = 3
        if li[i][j] == '*' :
            q.append([j,i,0,1])
for i in range(R) :
    for j in range(C) :
        if li[i][j] == 'S' :
            q.append([j,i,0,0])
            check[i][j] = 1
def bfs() :
    while q :
        x,y,v,c = q.popleft()
        if li[y][x] == 'D' and c == 0:
            return v
        # Case Water
        if c == 1:
            for i in range(4) :
                x_ = x + dx[i]
                y_ = y + dy[i]
                if x_ < 0 or x_ > C-1 or y_ < 0 or y_ > R-1 :
                    continue
                if check[y_][x_] != 2 and check[y_][x_] != 3:
                    check[y_][x_] = 2
                    q.append([x_,y_,v+1,1])
        # Case Beaver
        else :
            for i in range(4) :
                x_ = x + dx[i]
                y_ = y + dy[i]
                if x_ < 0 or x_ > C-1 or y_ < 0 or y_ > R-1 :
                    continue
                if not check[y_][x_] or check[y_][x_] == 3:
                    check[y_][x_] = 1
                    q.append([x_,y_,v+1,0])
    return "KAKTUS"
print(bfs()) 

# 더 깔끔한 풀이
import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]

R,C = map(int,input().split())
li = [list(input().rstrip()) for _ in range(R)]
check = [[0]*C for _ in range(R)]
q = deque()
for x in range(C) :
    for y in range(R) :
        if li[y][x] == "*" :
            q.append([x,y,0,1])
        elif li[y][x] == "S" :
            check[y][x] = 1
            a,b = x,y
def bfs() :
    q.append([a,b,0,0])
    while q :
        x,y,v,c = q.popleft()
        if c :
            for i in range(4) :
                x_ = x + dx[i]
                y_ = y + dy[i]
                if x_ < 0 or x_ > C-1 or y_ < 0 or y_ > R-1 :
                    continue
                if li[y_][x_] == "." :
                    li[y_][x_] = '*'
                    q.append([x_,y_,v+1,1])
        else :
            for i in range(4) :
                x_ = x + dx[i]
                y_ = y + dy[i]
                if x_ < 0 or x_ > C-1 or y_ < 0 or y_ > R-1 :
                    continue
                if li[y_][x_] == "." and not check[y_][x_] :
                    check[y_][x_] = 1
                    q.append([x_,y_,v+1,0])
                elif li[y_][x_] == 'D' :
                    return v+1
    return "KAKTUS"
print(bfs())