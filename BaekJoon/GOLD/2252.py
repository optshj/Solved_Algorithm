# 백준 2252번 줄 세우기
# GOLD 3
# 알고리즘 분류 : 그래프 이론, 위상 정렬
# 큰순서대로 그래프를 만든다음 위상정렬하면 되는 문제
from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
g = [[] for i in range(N+1)]
degree = [0] *(N+1)
for _ in range(M) :
    A,B = map(int,input().split())
    g[A].append(B)
    degree[B] += 1
result = []
q = deque()
for i in range(1,N+1) :
    if degree[i] == 0 :
        q.append(i)
while q :
    v = q.popleft()
    result.append(v)
    for i in g[v] :
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)
print(*result)