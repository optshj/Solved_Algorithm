#2292¹ø ¹úÁý
#BRONZE 2
a = int(input())
b = a//6
low = 1
high = 1
i = 1
while True :
    if low <= a and a <= high :
        break
    else :
        low = high + 1
        high = high + i*6
        i += 1
print(i)