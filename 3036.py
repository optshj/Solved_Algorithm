#3036¹ø ¸µ
#SILVER 3
import sys
def gcd(a,b):
    while b != 0:
        res = a%b
        a = b
        b = res
    return a
input = sys.stdin.readline
N = int(input())
li = list(map(int,input().split()))
li_1 = li[0]

for i in range(1,N):
    k = gcd(li_1,li[i])
    print(f"{li_1//k}/{li[i]//k}")