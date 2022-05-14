#2490¹ø À·³îÀÌ
#BRONZE 3
for i in range(3) :
    a = list(map(int,input().split()))
    b = a.count(0)
    if b == 0 :
        print('E')
    elif b == 1 :
        print('A')
    elif b == 2 :
        print('B')
    elif b == 3 :
        print('C')
    elif b == 4 :
        print('D')