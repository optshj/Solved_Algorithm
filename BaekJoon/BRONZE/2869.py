#2869�� �����̴� �ö󰡰� �ʹ�
#BROZNE 1
import sys
A,B,V = map(int,sys.stdin.readline().split())
if (V-A)%(A-B) > 0 :
    print((V-A)//(A-B) + 2)
else :
    print((V-A)//(A-B) + 1)