# 백준 13913번 숨바꼭질 4
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
# check 배열에 이전에 탐색했던 곳을 저장하고 나서 이후에 방문한 곳을 역추적 하는 문제
# check 배열을 0 으로 초기화 해서 시간초과가 났던 문제
from collections import deque
move = [1,-1]
N,K = map(int,input().split())
check = [-1]*(100001)
def bfs() :
    q = deque()
    q.append([N,0])
    check[N] = N
    while q :
        v,t = q.popleft()
        if v == K :
            return t
        for i in range(3) :
            if i == 2 :
                v_ = v*2
            else :
                v_ = v + move[i]
            if v_ < 0 or v_ > 100000:
                continue
            if check[v_] == -1:
                q.append([v_,t+1])
                check[v_] = v
print(bfs())
ans = [K]
val = K
while True :
    if val == N :
        break
    val = check[val]
    ans.append(val)
print(*ans[::-1])