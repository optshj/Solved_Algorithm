#2609번 최대공약수와 최소공배수
#SILVER 5
a , b = map(int,input().split())
if a < b :
    a , b = b , a
for i in range(1,a+1) :
    if a%i == 0 and b%i == 0 :
        gcd = i
print(gcd)
A = a
B = b
while True :
    if a == b :
        break
    if a > b :
        b += B
    elif a < b :
        a += A
print(a)