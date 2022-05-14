#1269번 대칭 차집합
#SILVER 3
import sys
input = sys.stdin.readline
A,B = map(int,input().split())
li1 = set(map(int,input().split()))
li2 = set(map(int,input().split()))
li3 = li1 & li2
print(A+B-2*len(li3))