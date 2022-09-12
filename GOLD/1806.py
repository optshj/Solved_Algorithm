# 백준 1806번 부분합
# GOLD 4
# 알고리즘 분류 : 누적 합, 두 포인터
N,S = map(int,input().split())
li = list(map(int,input().split())) + [0]
sum = li[0]
low = 0
high = 0
ans = N+1
while low <= high and high < N :
    if sum >= S :
        ans = min(ans,high-low+1)
        sum -= li[low]
        low += 1
    else :
        high += 1
        sum += li[high]
if ans == N+1 :
    print(0)
else :
    print(ans)