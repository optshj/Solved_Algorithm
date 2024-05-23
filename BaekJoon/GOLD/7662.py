# 백준 7662번 이중 우선순위 큐
# GOLD 4
# 알고리즘 분류 : 자료 구조, 트리를 사용한 집합과 맵, 우선순위 큐
# 최소힙과 최대힙 두개를 사용하여 구현하여 set으로 출력하는 것 까지 구현하였으나 안돼서 질문 게시판을 봄

import heapq
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    k = int(input())
    min_q = []
    max_q = []
    now = 0
    check = {}
    for i in range(k) :
        order, num = map(str,input().split())
        num = int(num)
        if order == 'I' :
            heapq.heappush(min_q,(num,num))
            heapq.heappush(max_q,(-num,num))
            if num not in check :
                check[num] = 1
            else :
                check[num] += 1
            now += 1
        else :
            try :
                if num == 1 :
                    max_val = heapq.heappop(max_q)[1]
                    while check[max_val] == 0 :
                        max_val = heapq.heappop(max_q)[1]
                    check[max_val] -= 1
                else :
                    min_val = heapq.heappop(min_q)[1]
                    while check[min_val] == 0 :
                        min_val = heapq.heappop(min_q)[1]
                    check[min_val] -= 1
                now -= 1
            except :
                continue
    if now <= 0 :
        print('EMPTY')
    else :
        li1 = []
        li2 = []
        while max_q :
            li1.append(heapq.heappop(max_q)[1])
        while min_q :
            li2.append(heapq.heappop(min_q)[1])
        s = list(set(li1) & set(li2))
        s.sort()
        print(s[-1],s[0])