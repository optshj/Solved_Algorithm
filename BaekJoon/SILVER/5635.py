#5635¹ø »ıÀÏ
#SILVER 5
n = int(input())
li = []
for i in range(n) :    
    a , b ,c , d= map(str,input().split())
    b = int(b)
    c = int(c)
    d = int(d)
    li.append([d,c,b,a])
    li.sort()
print(li[n-1][3])
print(li[0][3])