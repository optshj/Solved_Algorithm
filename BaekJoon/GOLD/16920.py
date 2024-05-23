# 백준 16920번 확장 게임
# GOLD 2
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
# 확장을 일자로 하는게 아니라 꺾을 수도 있음.
import sys
from collections import deque
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]
N,M,P = map(int,input().split())
S = [0] + list(map(int,input().split()))
check = [[0]*M for _ in range(N)]
li = [list(input().rstrip()) for _ in range(N)]
cnt = [0]*(P+1)
q = [deque() for _ in range(10)]
for i in range(N) :
    for j in range(M) :
        for p in range(1,P+1) :
            if li[i][j] == str(p) :
                check[i][j] = 1
                q[p].append([j,i])
                cnt[p] += 1
def bfs() :
    while True :
        flag = 1
        for i in range(1,10) :
            if q[i] :
                flag = 0
        for i in range(1,P+1) :
            for _ in range(S[i]) :
                if len(q[i]) == 0 :
                    break
                for j in range(len(q[i])) :    
                    x,y = q[i].popleft()
                    for k in range(4) :
                        x_ = x + dx[k]
                        y_ = y + dy[k]
                        if x_ < 0 or x_ > M-1 or y_ < 0 or y_ > N-1 :
                            continue
                        if li[y_][x_] == '.' and not check[y_][x_] :
                            check[y_][x_] = 1
                            q[i].append([x_,y_])
                            cnt[i] += 1
        if flag :
            break
bfs()
for i in range(1,P+1) :
    print(cnt[i],end = ' ')