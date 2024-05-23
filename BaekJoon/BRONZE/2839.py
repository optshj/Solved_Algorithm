#2839¹ø ¼³ÅÁ ¹è´Þ
#BRONZE 1
a = int(input())
result = 0
for i in range(1000,0,-1) :
    if a-5*i >= 0 and (a-5*i)%3 == 0:
        result += i
        a = a-5*i
        break
for i in range(1000,0,-1) :
    if a-3*i >= 0 :
        result += i
        a = a-3*i
        break
if a == 0 :
    print(result)
else :
    print(-1)