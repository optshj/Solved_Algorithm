# 백준 9019번 DSLR
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
# 내 풀이 (굉장히 난잡하다)
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
def bfs(n) :
    q = deque()
    q.append([n,''])
    check[n] = 1
    while q :
        n,a = q.popleft()
        if n == B :
            return a
        if not check[(n*2)%10000] :
            check[(n*2)%10000]
            q.append([(n*2)%10000,a+'D'])
        if n == 0 :
            if not check[9999] :
                check[9999] = 1
                q.append([9999,a+'S'])
        else :
            if not check[n-1] :
                check[n-1] = 1
                q.append([n-1,a+'S'])
        d1 = n//1000
        d2 = (n//100-d1*10)
        d3 = (n//10-d1*100-d2*10)
        d4 = n%10
        if not check[d2*1000+d3*100+d4*10+d1] :
            check[d2*1000+d3*100+d4*10+d1] = 1
            q.append([d2*1000+d3*100+d4*10+d1,a+"L"])

        if not check[d4*1000+d1*100+d2*10+d3] :
            check[d4*1000+d1*100+d2*10+d3] = 1
            q.append([d4*1000+d1*100+d2*10+d3,a+"R"])

for _ in range(T) :
    A,B = map(int,input().split())
    check = [0]*(10001)
    print(bfs(A))

# 가독성 UP
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
def bfs(v) :
    q = deque()
    q.append([v,''])
    check[v] = 1
    while q :
        v,a = q.popleft()
        if v == B :
            return a
        d = (2*v)%10000
        s = (v+9999)%10000
        l = (v%1000)*10 + v//1000
        r = (v%10)*1000 + v//10
        li = [d,s,l,r]
        for i,v in enumerate(li) :
            if not check[v] :
                check[v] = 1
                if i == 0 :
                    q.append([v,a+"D"])
                elif i == 1 :
                    q.append([v,a+"S"])
                elif i == 2 :
                    q.append([v,a+"L"])
                else :
                    q.append([v,a+"R"])

for _ in range(T) :
    A,B = map(int,input().split())
    check = [0]*10000
    print(bfs(A))