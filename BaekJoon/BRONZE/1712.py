#1712�� ���ͺб���
#BRONZE 4
import sys
a,b,c = map(int,sys.stdin.readline().split())
i = 1
if b >= c :
    print(-1)
else :
    print(a//(c-b)+1)