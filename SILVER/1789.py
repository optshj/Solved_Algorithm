#1789번 수들의 합
#SILVER 5
a = int(input())
b = 1
ans = 0
while True :
    a = a - b
    if a >= 0 :
        b += 1
        ans += 1
    elif a <= 0 :
        break
print(ans)