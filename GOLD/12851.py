# 백준 12851번 숨바꼭질 2
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
from collections import deque
N,K = map(int,input().split())
check = [0]*100001
cnt = 1
ans = 10000000
def bfs() :
    global cnt
    global ans
    q = deque()
    q.append([N,0])
    while q :
        v,c = q.popleft()
        check[v] = 1
        if v == K :
            if ans > c :
                ans = c
            elif ans == c :
                cnt += 1
        for i in [v+1,v-1,v*2] :
            if i < 0 or i > 100000 :
                continue
            if not check[i]:
                q.append([i,c+1])
bfs()
print(ans)
print(cnt)