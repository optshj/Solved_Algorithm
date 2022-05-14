#2740¹ø Çà·Ä °ö¼À
#BRONZE 1
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
li1 = []
li2 = []
for _ in range(N) :
    li1.append(list(map(int,input().split())))
M,K = map(int,input().split())
for _ in range(M) :
    li2.append(list(map(int,input().split())))
res = [[0]*K for _ in range(N)]
for i in range(N) :
    for j in range(K) :
        sum = 0
        for m in range(M) :
            sum += li1[i][m]*li2[m][j]
        res[i][j] += sum
for i in res :
    print(*i)