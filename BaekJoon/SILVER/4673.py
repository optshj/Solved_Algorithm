#4673¹ø ¼¿ÇÁ ³Ñ¹ö
#SILVER 5
li = []
for a in range(1,10001):
    if a < 10 :
        m1 = a
        li.append(a+m1)

    elif a < 100 :
        m1 = a%10 
        m2 = a//10
        li.append(a+m1+m2)

    elif a < 1000 :
        m1 = a%10
        m2 = (a%100-m1)//10
        m3 = a//100
        li.append(a+m1+m2+m3)
    else :
        m1 = a%10
        m2 = (a%100-m1)//10
        m3 = (a%1000-m1-m2)//100
        m4 = a//1000
        li.append(a+m1+m2+m3+m4)

for i in range(1,10001):
    if i not in li :
        print(i)