#2309¹ø ÀÏ°ö ³­ÀïÀÌ
#BRONZE 1
import sys
li = []
for _ in range(9) :
    li.append(int(sys.stdin.readline()))
li_sum = sum(li)
a = 0
b = 0
for i in range(8):
    for j in range(i+1,9):
        if (li_sum-(li[i]+li[j])) == 100:
            a = i
            b = j
li[a] = 100
li[b] = 100
li.sort()
for i in range(7):
    print(li[i])