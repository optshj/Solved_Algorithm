# 백준 1039번 교환
# GOLD 3
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
# check 배열 크기를 이상하게 만들어서 메모리초과가 났던 문제
from collections import deque
from copy import deepcopy
def parse_int(a) :
    return int(''.join(map(str,a)))
def bfs() :
    ans = -1
    q = deque()
    q.append([N,0])
    check[parse_int(N)][0] = 1
    while q :
        v,c = q.popleft()
        if c > K :
            continue
        if c == K :
            ans = max(ans,int(''.join(map(str,v))))
            continue
        for i in range(len(N)) :
            for j in range(i+1,len(N)) :
                v_ =  deepcopy(v)
                v_[i],v_[j] = v_[j],v_[i]
                val = parse_int(v_)
                if v_[0] == 0 :
                    continue
                if not check[val][c+1] :
                    q.append([v_,c+1])
                    check[val][c+1] = 1
    return ans

N,K = map(int,input().split())
N = list(map(int,str(N)))
check = [[0]*(K+1) for _ in range(1000001)]
print(bfs())