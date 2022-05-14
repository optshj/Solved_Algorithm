#1110번 더하기 사이클
#BRONZE 1
i = 0
a = int(input())
result = a

while True :
    if result >= 10 :
        m = result//10
        n = result%10
    else :
        m = 0
        n = result
    if m + n >= 10:
        k = m + n - 10
    else :
        k = m + n
    result = n*10 + k
    
    i += 1

    if a == result :
        break
print(i)