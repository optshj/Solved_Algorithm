#1259�� �Ӹ���Ҽ�
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