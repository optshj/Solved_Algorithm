# 백준 24445번 알고리즘 수업 - 너비 우선 탐색 2
# SILVER 2
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline
N,M,R = map(int,input().split())
visited = [0]*(N+1)
g = [[] for _ in range(N+1)]
count = [0 for _ in range(N+1)]
cnt = 1
for i in range(M) :
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
li = deque()
for i in g :
    i.sort(reverse=True)
def bfs(v) :
    global cnt
    visited[v] = 1
    count[v] = cnt
    li.append(v)
    while (len(li) != 0) :
        v = li.popleft()
        for i in g[v] :
            if not visited[i] :
                cnt += 1
                visited[i] = 1
                li.append(i)
                count[i] = cnt
bfs(R)
print(*count[1:],sep='\n')