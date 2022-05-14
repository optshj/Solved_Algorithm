#2805번 나무 자르기
#SILVER 2
import sys
input = sys.stdin.readline
N ,M = map(int,input().split())
li = list(map(int,input().split()))
low = 0
high = max(li)

while True :
    mid = (low+high)//2
    k = sum([(i - mid) for i in li if i > mid])
    
    if high < low:
        break
    if k >= M :
        low = mid + 1
    else :
        high = mid - 1
print(mid)