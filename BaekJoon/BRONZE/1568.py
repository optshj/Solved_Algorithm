#1568¹ø »õ
#BRONZE 2
n = int(input())
cnt = 0
i = 1
while n !=0 :
    if n < i :
        i = 1
    n -= i
    cnt += 1
    i += 1
print(cnt)