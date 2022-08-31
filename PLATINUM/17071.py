# 백준 17071번 숨바꼭질 5
# PLATINUM 5
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
# 풀다가 이상해서 찾아봄
# 수빈이가 찾아가면서 동생도 움직이는게 포인트 수빈이가 방문한 곳에 동생이 방문하면 리턴
# 짝수 시간에 방문한 곳은 좌 우로 움직여서 +2초 뒤에 또 방문 할 수 있다. 홀수 시간도 마찬가지
from collections import deque
N,K = map(int,input().split())
move = [1,-1]
check = [[0]*500001 for _ in range(2)]
q = deque()
q.append(N)
check[0][N] = 1
def bfs() :
    global K
    ans = 0
    while q :
        K += ans
        if K > 500000 :
            return -1
        for _ in range(len(q)) :
            v = q.popleft()
            for i in range(3) :
                if i == 2 :
                    v_ = v*2
                else :
                    v_ = v + move[i]
                if v_ < 0 or v_ > 500000 :
                    continue
                if not check[(ans+1)%2][v_] :
                    q.append(v_)
                    check[(ans+1)%2][v_] = 1
        if check[ans%2][K] :
            return ans
        ans += 1
    return -1
print(bfs())