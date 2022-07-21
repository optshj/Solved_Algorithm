# 백준 12852번 1로 만들기 2
# SILVER 1
# 알고리즘 분류 : 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색
from collections import deque
N = int(input())
check = [0]*(N+1)
res = [1]
def bfs(v) :
    q = deque()
    q.append([v,0])
    check[v] = 1

    while q :
        v,m = q.popleft()
        if v == 1 :
            break
        if v%3 == 0 and not check[v//3]:
            q.append([v//3,m+1])
            check[v//3] = v
        if v%2 == 0 and not check[v//2]:
            q.append([v//2,m+1])
            check[v//2] = v
        if not check[v-1] :
            q.append([v-1,m+1])
            check[v-1] = v
    return m
print(bfs(N))
while res[-1] != N :
    res.append(check[res[-1]])
print(*res[::-1])