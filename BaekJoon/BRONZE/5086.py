#5086번 배수와 약수
#BROZNE 3
while True :
    a,b = map(int,input().split())
    if a < b :
        if b%a == 0 :
            print('factor')
        else :
            print('neither')
    elif a > b :
        if a%b == 0 :
            print('multiple')
        else :
            print('neither')
    if a == 0 and b == 0 :
        break