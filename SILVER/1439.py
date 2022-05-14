#1439번 뒤집기
#SILVER 5
import sys
a = input()
re1 = []
re2 = []
for i in a.split('1') :
    if i != '' :
        re1.append(i)
for i in a.split('0') :
    if i != '' :
        re2.append(i)
print(min(len(re1),len(re2)))