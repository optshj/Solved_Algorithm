#9012¹ø °ýÈ£
#SILVER 4
import sys
a = int(sys.stdin.readline())
for i in range(a):
    b = list(str(sys.stdin.readline().rstrip()))
    check = 0
    for k in b:
        if k =='(':
            check += 1
        else:
            check -= 1
            if check < 0:
                break
    if check == 0:
        print("YES")
    else :
        print("NO")