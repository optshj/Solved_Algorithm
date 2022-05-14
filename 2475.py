#2475번 검증수
#BRONZE 5
a = list(map(int,input().split()))
result = 0
for i in range(5):
    result += a[i]**2
print(result%10)