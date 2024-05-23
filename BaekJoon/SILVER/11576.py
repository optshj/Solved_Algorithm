# 백준 11576번 Base Conversion
# SILVER 5
# 메모리 : 30840 KB , 시간 : 68ms , 언어 : Python3 , 코드길이 : 276B
A,B = map(int,input().split())
m = int(input())
li = list(map(int,input().split()))
result = 0
for i in range(m) :
    result += li[-i-1]*(A)**(i)
k = 0
while result > B**k :
    k += 1
for i in range(k-1,-1,-1) :
    print(result//(B**i),end = ' ')
    result = result%(B**i)