#6591번 이항 쇼다운
#SILVER 3
import sys
import math
while True :
    A,B = map(int,sys.stdin.readline().split())
    if A+B == 0 :
        break
    a = 1
    b = 1
    for i in range(A,max(A-B,B),-1):
        a *= i
    for i in range(1,min(A-B,B)+1):
        b *= i
    print(a//b)