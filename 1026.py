#1026¹ø º¸¹°
#SILVER 4
import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
result = 0
A.sort()
B.sort()
B.reverse()
for i in range(N):
    result += A[i]*B[i]
print(result)