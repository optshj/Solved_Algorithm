# 백준 2960번 에라토스테네스의 체
# SILVER 4
# 알고리즘 분류 : 수학,구현,정수론,소수 판정,에라토스테네스의 체
# 메모리 : 30840KB, 시간 : 68ms, 언어 : Python3, 코드 길이 : 344B
N,K = map(int,input().split())
cnt = 0
check = [True]*(N+1)
m = 0
for i in range(2,N+1) :
    if check[i] :
        for j in range(i,N+1,i) :
            if check[j]:
                cnt += 1
                check[j] = False
                k = j
            if cnt == K :
                print(k)
                break
    if m :
        break