#1259번 팰린드롬수
#BRONZE 1
while True :
    a = str(input())
    res = True
    if a == '0' :
        break
    for i in range(0,len(a)//2):
        if a[i] != a[-i-1]:
            res = False
    if res :
        print("yes")
    else :
        print("no")