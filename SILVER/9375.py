#9375¹ø ÆÐ¼Ç¿Õ ½ÅÇØºó
#SILVER 3
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    res = {}
    n = int(input())
    for i in range(n):
        value , key = input().split()
        if key not in res.keys():
            res[key] = [value]
        else :
            res[key].append(value)
    cnt = 1
    for key in res:
        cnt *= (len(res[key])+1)
    print(cnt-1)