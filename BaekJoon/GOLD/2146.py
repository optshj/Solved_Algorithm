# 백준 2146번 다리 만들기
# GOLD 3
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
# Python3 시간 초과 Pypy3 AC
import sys
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
input = sys.stdin.readline
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
check = [[0]*N for _ in range(N)]
res = []
ans = 10000
def bfs(x,y) :
    val = []
    q = deque()

    q.append([x,y])
    val.append([x,y])

    check[x][y] = 1
    
    while q :
        x,y = q.popleft()
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
                continue
            if li[x_][y_] and not check[x_][y_] :
                q.append([x_,y_])
                check[x_][y_] = 1
                val.append([x_,y_])
    res.append(val)

for i in range(N) :
    for j in range(N) :
        if li[i][j] and not check[i][j] :
            bfs(i,j)

for i in range(len(res)) :
    for j in range(len(res)) :
        if i == j :
            continue
        for n in range(len(res[i])) :
            for m in range(len(res[j])) :
                ans = min(ans,abs(res[i][n][0]-res[j][m][0])+abs(res[i][n][1]-res[j][m][1]))
print(ans-1)

# Python3 AC
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
check = [[0]*N for _ in range(N)]
distance = [[0]*N for _ in range(N)]
distnace_q = deque()
ans = 200
cnt = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(x,y) :
    q = deque()
    q.append([x,y])
    distnace_q.append([x,y])
    check[x][y] = cnt
    while q :
        x,y = q.popleft()
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
                continue
            if li[x_][y_] and not check[x_][y_] :
                check[x_][y_] = cnt
                q.append([x_,y_])
                distnace_q.append([x_,y_])

for i in range(N) :
    for j in range(N) :
        if li[i][j] and not check[i][j] :
            cnt += 1
            bfs(i,j)
while distnace_q :
    x,y = distnace_q.popleft()
    for i in range(4) :
        x_ = x + dx[i]
        y_ = y + dy[i]
        if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
            continue
        if li[x_][y_] == 0 and not check[x_][y_] :
            distance[x_][y_] = distance[x][y] + 1
            check[x_][y_] = check[x][y]
            distnace_q.append([x_,y_])
for x in range(N) :
    for y in range(N) :
        for k in range(4) :
            x_ = x + dx[k]
            y_ = y + dy[k]
            if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
                continue
            if check[x][y] != check[x_][y_] :
                ans = min(ans,distance[x][y] + distance[x_][y_])
print(ans)