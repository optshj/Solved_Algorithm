#1011번 Fly me to the Alpha Centauri
#GOLD 5
import sys
import math

a = int(input())
for i in range(a) :
    x,y = map(int,sys.stdin.readline().split())
    distance = y-x
    max = int(math.sqrt(distance))
    if max**2 == distance :
        print(2*max-1)
    elif distance <= max**2 + max:
        print(2*max)
    else :
        print(2*max + 1)