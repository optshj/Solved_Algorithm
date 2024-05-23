#3273번 두 수의 합
#SILVER 3
import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))
x = int(input())
li.sort()
cnt = 0
s = 0
e = n - 1
while s < e :
    li_sum = li[s] + li[e]
    if li_sum == x :
        cnt += 1
    elif li_sum > x :
        e -= 1
        continue
    s += 1
print(cnt)