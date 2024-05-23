#1924¹ø 2007³â
#BRONZE 1
import sys
x,y = map(int,sys.stdin.readline().split())
k = [31,28,31,30,31,30,31,31,30,31,30,31]
l = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
r = y
for i in range(1,x):
    r+= k[i-1]
print(l[r%7])