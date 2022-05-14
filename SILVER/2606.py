#2606번 바이러스
#SILVER 3
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
li = [list(map(int,input().split())) for _ in range(M)]
check = [False]*(N+1)
check[1] = True
for i in range(M) :
    for j in range(M) :
        if check[li[j][0]] or check[li[j][1]] :
            check[li[j][0]] = check[li[j][1]] = True
print(check.count(True)-1)