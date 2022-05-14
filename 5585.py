#5585¹ø °Å½º¸§µ·
#BRONZE 2
a = 1000 - int(input())
li = [500,100,50,10,5,1]
cnt = 0
for i in li :
    if a//i > 0 :
        cnt += a//i
        a = a%i
print(cnt)