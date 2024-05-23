# 백준 1300번 K번째 수
# GOLD 2
# 알고리즘 분류 : 이분 탐색, 매개 변수 탐색
# mid보다 작은수의 개수는 mid//i 이므로 각 i 에 대해 mid//i를 구한뒤
# 현재 mid보다 작은수의 개수를 구함 
N = int(input())
K = int(input())
low = 0
high = 10**10
answer = 0
while True :
    mid = (high+low)//2
    if low > high :
        break
    ans = 0
    for i in range(1,N+1) :
        ans += min(mid//i,N)
    if ans >= K :
        answer = mid
        high = mid - 1
    else :
        low = mid + 1
print(answer)