# 백준 15711번 환상의 짝꿍
# GOLD 3
# 알고리즘 분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체
import sys

input = sys.stdin.readline
N = 2 * 10**6
era = [0, 0] + [1] * (N - 1)
primes = []

for i in range(2, N + 1):
    if era[i]:
        primes.append(i)
        for j in range(2 * i, N + 1, i):
            era[j] = 0

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    S = A + B
    if S < 4 :
      print("NO")
    elif S % 2 == 0:
        print("YES")
    else:
        for i in primes:
            if i * i > (S - 2):
                print("YES")
                break
            elif (S - 2) % i == 0:
                print("NO")
                break
        else :
          print("YES")
