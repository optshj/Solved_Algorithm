# 백준 16946번 벽 부수고 이동하기 4
# GOLD 2
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# 탐색하면서 0인 곳에 넘버링을 함
import sys
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
input = sys.stdin.readline
N,M = map(int,input().split())
li = [list(map(int,input().rstrip())) for _ in range(N)]
ans = [[0]*M for _ in range(N)]
check = [[0]*M for _ in range(N)]
val = [0]
cnt = 0
def bfs(x,y) :
    a = 1
    q = deque()
    q.append([x,y])
    check[y][x] = cnt
    while q :
        x,y = q.popleft()
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > M-1 or y_ < 0 or y_ > N-1 :
                continue
            if li[y_][x_] == 0 and not check[y_][x_] :
                q.append([x_,y_])
                check[y_][x_] = cnt
                a += 1
    return a
for i in range(N) :
    for j in range(M) :
        if li[i][j] == 0 and not check[i][j]:
            cnt += 1
            val.append(bfs(j,i))
for i in range(N) :
    for j in range(M) :
        if li[i][j] :
            ans[i][j] += 1
            visit = set()
            for _ in range(4) :
                i_ = i + dy[_]
                j_ = j + dx[_]
                if i_ < 0 or i_ > N-1 or j_ < 0 or j_ > M-1 :
                    continue
                visit.add(check[i_][j_])
            for _ in visit :
                ans[i][j] += val[_]
        print(ans[i][j]%10,end='')
    print()