# 백준 24472번 알고리즘 수업 - 깊이 우선 탐색 1
# SILVER 2
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 정렬, 깊이 우선 탐색
# 메모리 : 171836KB, 시간 : 680ms, 언어 : Python3, 코드 길이 : 462B
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,M,R = map(int,input().split())
check = [0]*(N+1)
cnt = 0
count = [0 for _ in range(N+1)]
g = [[] for _ in range(N+1)]
for i in range(M) :
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
def dfs(v):
    global cnt
    cnt += 1
    check[v] = 1
    count[v] = cnt
    for i in sorted(g[v]) :
        if not check[i] :
            dfs(i)
dfs(R)
print(*count[1:],sep='\n')