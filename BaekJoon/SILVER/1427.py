#1427번 소트인사이드
#SILVER 5
import sys
a = list(map(int,sys.stdin.readline().strip()))
a.sort()
a.reverse()
for i in a :
    print(i,end='')