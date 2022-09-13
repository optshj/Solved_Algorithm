# 백준 24164번 光ファイバー網の整備 (Fiber)
# SILVER 2
# 알고리즘 분류 : 그래프 이론, 자료 구조, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 분리집합
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
g = [[] for _ in range(N+1)]
check = [0]*(N+1)
ans = 0
def bfs(v) :
    global ans
    ans += 1
    q = deque()
    q.append(v)
    check[v] = 1
    while q :
        v = q.popleft()
        for i in g[v] :
            if not check[i] :
                q.append(i)
                check[i] = 1
for _ in range(M) :
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(1,N+1) :
    if not check[i] :
        bfs(i)
print(ans-1)