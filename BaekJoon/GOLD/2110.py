# 백준 2110번 공유기 설치
# GOLD 5
# 알고리즘 분류 : 이분 탐색, 매개 변수 탐색
# 메모리 38568KB, 시간 588ms ,언어 Python3 ,코드길이 :482B
import sys
input = sys.stdin.readline
N,C = map(int,input().split())
li = [int(input()) for _ in range(N)]
li.sort()
def check(mid) :
    k = 0
    cnt = 1
    for i in range(N) :
        if li[k] + mid <= li[i] :
            k = i
            cnt += 1
    return cnt
low = 1
high = li[-1] - li[0]
val = 0
while True :
    mid = (low+high)//2
    if high < low :
        break
    cnt = check(mid)
    if cnt >= C :
        low = mid + 1
    else :
        high = mid - 1
print(mid)