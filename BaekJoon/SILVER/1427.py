#1427�� ��Ʈ�λ��̵�
#SILVER 5
import sys
a = list(map(int,sys.stdin.readline().strip()))
a.sort()
a.reverse()
for i in a :
    print(i,end='')