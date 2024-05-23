# 백준 11054번 가장 긴 바이토닉 부분 수열
# GOLD 3
# 알고리즘 분류 : 다이나믹 프로그래밍
# 선택된 숫자에서 왼쪽으로 증가수열의 길이와 오른쪽으로 감소수열의 길이의 합을 구하고
# 그 합중에서 가장 큰 값 - 1을 출력한다.
N = int(input())
A = list(map(int,input().split()))
small = [0]*(N+1)
large = [0]*(N+1)
max_size = 0
for i in range(N) :
    max_val = 0
    for j in range(i) :
        if A[i] > A[j] :
            if small[j+1] > max_val :
                max_val = small[j+1]
    small[i+1] += max_val + 1

for i in range(N-1,-1,-1) :
    min_val = 0
    for j in range(N-1,i,-1) :
        if A[i] > A[j] :
            if large[j+1] > min_val :
                min_val = large[j+1]
    large[i+1] += min_val + 1
for i in range(N+1) :
    max_size = max(max_size,small[i]+large[i])
print(max_size-1)