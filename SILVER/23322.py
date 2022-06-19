# 백준 23322번 초콜릿 뺏어 먹기
# SILVER 3
# 알고리즘 분류 : 그리디 알고리즘, 애드 훅
N,K = map(int,input().split())
li = list(map(int,input().split()))
print(sum(li) - li[0]*N,N - li.count(li[0]))