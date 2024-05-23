#1764¹ø µèº¸Àâ
#SILVER 4
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
d = set()
b = set()
for _ in range(N):
    d.add(input().rstrip())
for _ in range(M):
    b.add(input().rstrip())
l = sorted(list(d&b))
print(len(l))
for i in l :
    print(i)