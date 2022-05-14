#1850번 최대공약수
#SILVER 2
def uclid(a,b):
    while b != 0 :
        temp = a%b
        a = b
        b = temp
    return a
a , b = map(int,input().split())
if a < b :
    a , b = b , a
print("1"*uclid(a,b))