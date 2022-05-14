#2004번 조합 0의 개수
#SILVER 2
import sys
a,b = map(int,input().split())
def five(a):
    cnt = 0
    while a != 0:
        a = a//5
        cnt += a
    return cnt

def two(a):
    cnt = 0
    while a != 0:
        a = a//2
        cnt += a
    return cnt
print(min(five(a)-five(b)-five(a-b),two(a)-two(b)-two(a-b)))