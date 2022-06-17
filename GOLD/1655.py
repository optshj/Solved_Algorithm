# 백준 1655번 가운데를 말해요
# GOLD 2
# 알고리즘 분류 : 자료 구조, 우선순위 큐
# 하위 1/2을 최대힙에 상위 1/2을 최소힙에 넣어 최대힙의 가장 작은수를 꺼낸다.
import heapq
import sys
input = sys.stdin.readline
min_h = []
max_h = []
N = int(input())
for _ in range(N) :
    k = int(input())
    if len(min_h) == len(max_h) :
        heapq.heappush(max_h,(-k,k))
    else :
        heapq.heappush(min_h,(k,k))
    if min_h and min_h[0][1] < max_h[0][1] :
        a = heapq.heappop(min_h)
        b = heapq.heappop(max_h)
        heapq.heappush(min_h,(-b[0],b[1]))
        heapq.heappush(max_h,(-a[0],a[1]))
    print(max_h[0][1])