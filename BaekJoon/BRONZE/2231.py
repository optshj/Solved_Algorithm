#2231번 분해합
#BRONZE 2
import sys
N = int(sys.stdin.readline())
mi = N - len(str(N))*9
if mi < 0 :
    mi = 1
for i in range(mi,N+1) :
        li = list(map(int,str(i)))
        if i + sum(li) == N :
            print(i)
            break
        if i == N :
            print(0)