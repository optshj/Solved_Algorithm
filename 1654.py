#1654번 랜선 자르기
#SILVER 3
import sys
input = sys.stdin.readline
N ,M = map(int,input().split())
li = []
for _ in range(N):
    li.append(int(input()))

low = 0
high = max(li)

while True :
    mid = (low+high)//2
    if high == 1:
        mid = 1
    k = sum([(i//mid) for i in li])
    
    if high < low:
        break
    if k >= M :
        low = mid + 1
    else :
        high = mid - 1
print(mid)