#1094번 막대기
#SILVER 5
import sys
a = int(input())
b = 64
c = 64
cnt = 1
while True :
    if b > a :
        c = c//2
        cnt += 1
        if b - c >= a :
            b = b - c
            cnt -= 1
    else :
        break
print(cnt)