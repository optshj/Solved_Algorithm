#1193번 분수찾기
#BRONZE 1
a = int(input())
low = 1
high = 1
i = 2

while True :
    if low <= a and a <= high :
        break
    else :
        low = high + 1
        high = high + i
        i = i + 1
a = a - high + i - 1
if i%2 == 0 :
    m = 1           #분모
    n = i - m       #분자
    while True :
        if a == 1 :
            break
        m = m + 1
        n = n - 1
        a = a - 1
    print(f'{n}/{m}')

elif i%2 == 1 :
    n = 1
    m = i - n
    while True :
        if a == 1 :
            break
        m = m - 1
        n = n + 1
        a = a - 1    
    print(f'{n}/{m}')