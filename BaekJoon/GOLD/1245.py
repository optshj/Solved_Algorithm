# 백준 1245번 농장 관리
# GOLD 5
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# 8방향 중에서 자기보다 높이가 큰 값이 없으면 봉우리다.
import sys
sys.setrecursionlimit(10**4)
N,M = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]
dx = [1,-1,1,-1,0,0,1,-1]
dy = [1,1,-1,-1,1,-1,0,0]
ans = 0
def dfs(x,y) :
    global val
    check[y][x] = 1
    for i in range(8) :
        x_ = x + dx[i]
        y_ = y + dy[i]
        if x_ < 0 or x_ > M-1 or y_ < 0 or y_ > N-1 :
            continue
        if li[y_][x_] > li[y][x] :
            val = 0
        if li[y_][x_] == li[y][x] and not check[y_][x_] :
            dfs(x_,y_)

for i in range(N) :
    for j in range(M) :
        if not check[i][j] :
            val = 1
            dfs(j,i)
            if val :
                ans += 1
print(ans)