# 백준 1271번 엄청난 부자2
# BRONZE 1
# 알고리즘 분류 : 수학, 사칙연산, 임의 정밀도/큰 수 연산
N,M = map(int,input().split())
print(N//M)
print(N-N//M*M)