# 백준 1939번 중량제한
# GOLD 3
# 알고리즘 분류 : 자료 구조, 그래프 이론, 그래프 탐색, 이분 탐색, 너비 우선 탐색, 분리 집합
import sys

from collections import deque

def bfs(my_list, value, start, end, n) :

    

  

    que = deque()

    v = [0 for _ in range(n+1)]

    

  

    v[start] = 1

    que.append(start)

    

    

    while que :

        asis = que.popleft()

        if asis == end :

            return True


        for togo, limit in my_list[asis]:

            if limit >= value and v[togo] == 0:

                que.append(togo)

                v[togo] = 1

    return False

n,m = map(int,sys.stdin.readline().split())

my_list = [[] for _ in range(n+1)]

for _ in range(m) :

    a,b,c = map(int,sys.stdin.readline().split())

    my_list[a].append((b,c))

    my_list[b].append((a,c))

s,e = map(int,sys.stdin.readline().split())

l,r = 0, sys.maxsize

answer = 0

while l < r :

    mid = (l + r +1 ) // 2

    if bfs(my_list, mid, s, e, n) :

        l = mid

        answer = mid

    else :

        r = mid - 1

print(answer)