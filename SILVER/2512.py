#2512¹ø ¿¹»ê
#SILVER 3
import sys
input = sys.stdin.readline
a = int(input())
b = sorted(list(map(int,input().split())))
c = int(input())
low = 0
high = b[a-1]
while True :
    mid = (low+high)//2
    if low > high :
        break
    k = sum([mid if i > mid else i for i in b])
    if k > c :
        high = mid - 1
    else :
        low = mid + 1
print(mid)