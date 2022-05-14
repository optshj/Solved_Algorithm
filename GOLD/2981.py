#2981¹ø °Ë¹®
#GOLD 5
import sys
import math
input = sys.stdin.readline
N = int(input())
li = []
for _ in range(N) :
    li.append(int(input()))
li.sort()
val = li[1] - li[0]
for i in range(2,N) :
    val = math.gcd(val,li[i]-li[i-1])
result = []
for i in range(2, int(val**0.5) + 1):
    if val % i == 0:
        result.append(i)
        result.append(val // i)
result.append(val)
print(*sorted(list(set(result))))