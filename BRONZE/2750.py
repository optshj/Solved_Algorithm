#2750번 수 정렬하기
#BROZNE 1
a = int(input())
li = []
for i in range(a) :
    n = int(input())
    li.append(n)
li = sorted(li)
for f in range(a) :
    print(li[f])