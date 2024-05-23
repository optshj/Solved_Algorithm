# 백준 2623번 음악프로그램
# GOLD 3
# 알고리즘 분류 : 그래프 이론, 위상 정렬
# i번째와 i+1 이 연결된 단방향 그래프로 생각해서 풀면 된다.
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
g = [[] for _ in range(N+1)]
q = deque()
indegree = [0]*(N+1)
ans = []
for _ in range(1,M+1) :
    li = list(map(int,input().split()))
    for i in range(1,li[0]) :
        g[li[i]].append(li[i+1])
        indegree[li[i+1]] += 1
for i in range(1,N+1) :
    if indegree[i] == 0 :
        q.append(i)
while q :
    v = q.popleft()
    ans.append(v)
    for i in g[v] :
        indegree[i] -= 1
        if indegree[i] == 0 :
            q.append(i)
if len(ans) != N :
    print(0)
else :
    print(*ans,sep='\n')