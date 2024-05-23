# 백준 1016번 제곱 ㄴㄴ 수
# GOLD 1
# 알고리즘 분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체
# 시간을 최대한 줄이기 위해 min~max 사이에서 i**2의 배수를 찾게 범위를 지정해줌
min,max = map(int,input().split())
era = [0]*(max-min+1)
for i in range(2,int(max**0.5)+1) :
    sqr = i**2
    for j in range(sqr*(min//sqr),max+1,sqr) :
        if j-min >= 0 :
            era[j-min] = 1
print(era.count(0))