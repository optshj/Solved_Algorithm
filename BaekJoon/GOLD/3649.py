# 백준 3649번 로봇 프로젝트
# GOLD 5
# 알고리즘 분류 : 정렬, 이분 탐색, 두 포인터
# 입력을 받는데 try except 로 받는게 핵심
import sys
input = sys.stdin.readline
while True :
    try :
        x = int(input())*10000000
        n = int(input())
        li = [int(input()) for _ in range(n)]
        li.sort()
        low = 0
        high = n-1
        check = 0
        while low < high :
            val = li[low] + li[high]
            if val == x :
                check = 1
                break
            if val < x :
                low += 1
            else :
                high -= 1
        if check :
            print(f"yes {li[low]} {li[high]}")
        else :
            print('danger')
    except :
        break