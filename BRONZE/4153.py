#4153번 직각삼각형
#BROZNE 3
while True :
    a,b,c = map(int,input().split())
    if a+b+c  == 0 :
        break
    li = [a,b,c]
    li = sorted(li)
    if li[0]**2+li[1]**2 == li[2]**2 :
        print('right')
    else :
        print('wrong')