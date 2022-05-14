#5063¹ø TGN
#BRONZE 3
a = int(input())
for i in range(a):
    m,n,k = map(int,input().split())
    if (n-k) < m :
        print('do not advertise')
    elif (n-k) > m :
        print('advertise')
    else :
        print ('does not matter')