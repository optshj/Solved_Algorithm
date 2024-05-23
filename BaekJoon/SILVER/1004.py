#1004번 어린 왕자
#SILVER 3
from math import sqrt
import sys

def check(a,b):
    global cnt
    if a == True and b == False :
        cnt += 1
    elif a == False and b == True :
        cnt += 1

def length(x1,y1,cx,cy,r):
    if sqrt((x1-cx)**2+(y1-cy)**2) < r:
        return True
    return False

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    x1,y1,x2,y2 = map(int,input().split())
    cnt = 0
    n = int(input())
    for i in range(n):
        cx,cy,r = map(int,input().split())
        case_1 = length(x1,y1,cx,cy,r)
        case_2 = length(x2,y2,cx,cy,r)
        check(case_1,case_2)
    print(cnt)