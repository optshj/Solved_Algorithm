# 백준 1068번 트리
# GOLD 5
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색
N = int(input())
li = list(map(int,input().split()))
v = int(input())
check = [0]*N
cnt = 0

def dfs(v) :
    check[v] = 1
    li[v] = - 1
    for i in range(N) :
        if v == li[i] :
            dfs(i)

dfs(v)
for i in range(N) :
    if check[i] == 0 and i not in li :
        cnt += 1
print(cnt)