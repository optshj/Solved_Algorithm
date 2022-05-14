#1966번 프린터 큐
#SILVER 3
import sys
input = sys.stdin.readline
a = int(input())


for _ in range(a):
    N,M = map(int,input().split())
    li = list(map(int,input().split()))
    result = list(range(0,N))
    l = []
    while len(result) != 0 :
        m = result.pop(0)
        if li[0] == max(li) :
            l.append(m)
            del li[0]

        else :
            b = li.pop(0)
            li.append(b)
            result.append(m)
    print(l.index(M)+1)