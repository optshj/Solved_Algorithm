# 백준 1707번 이분 그래프
# GOLD 4
# 알고리즘 분류 : 그래프
# 방문할때 1 또는 2로 색칠하면서 가까이 있는 노드가 색깔이 같으면 이분그래프가 아님
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(v,c) :
    check[v] = c
    for i in g[v] :
        if check[i] == 0 :
            if dfs(i,3-c) :
                return True
        elif check[i] == check[v] :
            return True

    return False
T = int(input())

for _ in range(T) :
    V,E = map(int,input().split())
    g = [[] for i in range(V+1)]
    bin = True
    check = [0]*(V+1)
    for i in range(E) :
        a,b = map(int,input().split())
        g[a].append(b)
        g[b].append(a)
    for i in range(1,V+1) :
        if check[i] == 0 :
            if dfs(i,1) :
                bin = False
                print("NO")
                break
    if bin :
        print("YES")
