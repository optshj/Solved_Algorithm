#1009번 분산처리
#BRONZE 3
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    k = 1
    for i in range(b):
        k = (k*a)%10
    if k == 0 :
        print(k+10)
    else :
        print(k)