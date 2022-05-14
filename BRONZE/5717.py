#5717번 상근이의 친구들
#BRONZE 3
import sys

while True :

    m , f = map(int,sys.stdin.readline().split())

    if m==0 and f==0 :
        break
    else :
        print(m+f)