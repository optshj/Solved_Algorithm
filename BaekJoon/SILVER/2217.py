#2217¹ø ·ÎÇÁ
#SILVER 4
import sys
input = sys.stdin.readline
N = int(input())
l = []
max = 0
for _ in range(N):
    l.append(int(input()))
l = sorted(l)
for i in range(N):
    k = N-i
    m = l[i]
    if m*k > max :
        max = m*k
print(max)