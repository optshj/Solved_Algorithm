# 백준 9466번 텀 프로젝트
# GOLD 3
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 깊이 우선 탐색
# 이전에 방문한 곳에 다시 방문하면 사이클이 존재한다는것.
# 사이클의 길이 = 방문했던 길이 - 사이클의 시작점의 index
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input())
def dfs(v) :
    global cnt
    check[v] = 1
    next = li[v]
    cycle.append(v)
    if check[next] :
        if next in cycle :
            cnt += len(cycle) - cycle.index(next)
    else :
        dfs(next)

for _ in range(T) :
    N = int(input())
    li = [0] + list(map(int,input().split()))
    check = [0]*(N+1)
    cnt = 0
    for i in range(1,N+1) :
        if not check[i] :
            cycle = []
            dfs(i)
    print(N - cnt)
# 위상 정렬 풀이
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    N = int(input())
    li = [0] + list(map(int,input().split()))
    indegree = [0]*(N+1)
    q = deque()
    g = [[] for _ in range(N+1)]
    result = []

    for i in range(1,N+1) :
        g[i].append(li[i])
        indegree[li[i]] += 1
    for i in range(1,N+1) :
        if indegree[i] == 0 :
            q.append(i)
    while q :
        now = q.popleft()
        result.append(now)
        for i in g[now] :
            indegree[i] -= 1
            if indegree[i] == 0 :
                q.append(i)
    print(len(result))