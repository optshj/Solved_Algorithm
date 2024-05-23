# 백준 11286번 절댓값 힙
# SILVER 1
# 알고리즘 분류 : 자료 구조, 우선순위 큐
# 메모리 42700KB, 시간 408ms ,언어 Python3 ,코드길이 : 305B
import sys
from queue import PriorityQueue
input = sys.stdin.readline
N = int(input())
queue = PriorityQueue(maxsize=100000)
for _ in range(N) :
    a = int(input())
    if a == 0 and queue.empty() :
        print(0)
    elif a == 0 :
        print(queue.get()[1])
    else :
        queue.put((abs(a),a))