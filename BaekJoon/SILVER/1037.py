#1037�� ���
#SILVER 5
import sys
N = int(sys.stdin.readline())
li = sorted(list(map(int,input().split())))
print(li[0]*li[len(li)-1])