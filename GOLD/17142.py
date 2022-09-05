# 백준 17142번 연구소 3
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색
from itertools import combinations
from collections import deque
import copy
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 1e9
def bfs() :
    ans = 0
    while q :
        x,y,v = q.popleft()
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
                continue
            if l[y_][x_] == 1 :
                continue
            if l[y_][x_] == 0 :
                ans = v + 1
            q.append([x_,y_,v+1])
            l[y_][x_] = 1
    return ans
N,M = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
lo = []
for i in range(N) :
    for j in range(N) :
        if li[i][j] == 2 :
            lo.append([j,i])
choose = combinations(lo,M)
for val in choose :
    q = deque()
    l = copy.deepcopy(li)
    for i in val :
        q.append([i[0],i[1],0])
    flag = 0
    cnt = bfs()
    for i in range(N) :
        for j in range(N) :
            if l[i][j] == 0 :
                flag = 1
                break
        if flag :
            break
    if flag == 0 :
        ans = min(ans,cnt)
print(-1 if ans == 1e9 else ans)
