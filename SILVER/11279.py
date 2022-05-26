# 백준 11279번 최대 힙
# SILVER 2
# 알고리즘 분류 : 자료 구조, 우선순위 큐
# 메모리 : 40496KB, 시간 : 388 ms, 언어 : Python3, 코드 길이 : 294B
import sys
from queue import PriorityQueue
input = sys.stdin.readline
N = int(input())
que = PriorityQueue(maxsize=100000)
for _ in range(N) :
    a = int(input())
    if a == 0 and que.empty():
        print(0)
    elif a == 0 :
        print((-1)*que.get())
    else :
        que.put((-1)*a)