#1072¹ø °ÔÀÓ
#SILVER 3
X,Y = map(int,input().split())
Z = 100*Y//X
if Z >= 99 :
    print(-1)
else :
    low = 0
    high = 10000000000
    while True :
        mid = (low+high)//2
        if low > high :
            break
        K = 100*(Y+mid)//(X+mid)
        if K > Z :
            high = mid - 1
        else :
            low = mid + 1
    print(mid+1)