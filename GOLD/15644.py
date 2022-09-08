# 백준 15644번 구슬 탈출 4
# GOLD 1
# 알고리즘 분류 : 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션
# 백준 13460번과 같은 문제 방향을 따로 출력해주는 조건 추가
from collections import deque
q = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def way(i) :
    if i == 0 :
        return 'R'
    elif i == 1 :
        return 'L'
    elif i == 2 :
        return 'D'
    else :
        return 'U'

def bfs() :
    time = 0
    while q :
        for _ in range(len(q)) :
            rx,ry,bx,by,a = q.popleft()
            if rx == ox and ry == oy :
                if time > 10 :
                    print(-1)
                    exit()
                print(time)
                print(a)
                exit()
            for i in range(4) :
                flag = 0
                rx_ = rx
                ry_ = ry
                bx_ = bx
                by_ = by
                while True :
                    rx_ += dx[i]
                    ry_ += dy[i]
                    if rx_ < 0 or rx_ > M-1 or ry_ < 0 or ry_ > N-1 or li[ry_][rx_] == '#' :
                        rx_ -= dx[i]
                        ry_ -= dy[i]
                        break
                    if li[ry_][rx_] == 'O' :
                        break
                while True :
                    bx_ += dx[i]
                    by_ += dy[i]
                    if bx_ < 0 or bx_ > M-1 or by_ < 0 or by_ > N-1 or li[by_][bx_] == '#' :
                        bx_ -= dx[i]
                        by_ -= dy[i]
                        break
                    if li[by_][bx_] == 'O' :
                        flag = 1
                        break
                if flag :
                    continue
                if rx_ == bx_ and ry_ == by_ :
                    if abs(rx_-rx) + abs(ry_-ry) > abs(bx_-bx) + abs(by_-by) :
                        rx_ -= dx[i]
                        ry_ -= dy[i]
                    else :
                        bx_ -= dx[i]
                        by_ -= dy[i]
                if not check[ry_][rx_][by_][bx_] :
                    q.append([rx_,ry_,bx_,by_,a+way(i)])
                    check[ry_][rx_][by_][bx_] = 1
        time += 1
    return -1

N,M = map(int,input().split())
li = [list(input()) for _ in range(N)]
check = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for i in range(N) :
    for j in range(M) :
        if li[i][j] == 'B' :
            bx,by = j,i
        elif li[i][j] == 'O' :
            ox,oy = j,i
        elif li[i][j] == 'R' :
            rx,ry = j,i
q.append([rx,ry,bx,by,''])
check[ry][rx][by][bx] = 1
print(bfs())