#9095번 1,2,3 더하기
#SILVER 3
import sys
input = sys.stdin.readline
T = int(input())
li = [0,1,2,4]
for i in range(4,12):
    li.append(li[i-3]+li[i-2]+li[i-1])
for _ in range(T):
    n = int(input())
    print(li[n])