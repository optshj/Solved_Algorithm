#2908¹ø »ó¼ö
#BRONZE 2
import sys
a , b = map(int,sys.stdin.readline().split())
m = a//100 + (a%100-a%10) +(a%10)*100
n = b//100 + (b%100-b%10) +(b%10)*100

if m > n :
    m , n = n , m
    
print(n)