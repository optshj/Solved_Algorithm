#1003번 피보나치 함수
#SILVER 3
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    cnt_0 = [1,0]
    cnt_1 = [0,1]
    for i in range(2,N+1):
        cnt_0.append(cnt_0[i-1]+cnt_0[i-2])
        cnt_1.append(cnt_1[i-1]+cnt_1[i-2])
    print(cnt_0[N],cnt_1[N])