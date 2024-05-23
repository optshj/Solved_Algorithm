#2869번 달팽이는 올라가고 싶다
#BROZNE 1
import sys
A,B,V = map(int,sys.stdin.readline().split())
if (V-A)%(A-B) > 0 :
    print((V-A)//(A-B) + 2)
else :
    print((V-A)//(A-B) + 1)