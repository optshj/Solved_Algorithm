# 백준 1766번 문제집
# GOLD 2
# 알고리즘 분류 : 그래프 이론, 자료 구조, 우선순위 큐, 위상 정렬
# 위상정렬할때 데이터를 우선순위 큐에 넣고 출력
import sys
import heapq
input = sys.stdin.readline
N,M = map(int,input().split())
g = [[] for i in range(N+1)]
degree = [0] *(N+1)
for _ in range(M) :
    A,B = map(int,input().split())
    g[A].append(B)
    degree[B] += 1
result = []
h = []
for i in range(1,N+1) :
    if degree[i] == 0 :
        heapq.heappush(h,i)
while h :
    v = heapq.heappop(h)
    result.append(v)
    for i in g[v] :
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(h,i)
print(*result)