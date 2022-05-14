#1158번 요세푸스 문제
#SILVER 4
N,K = map(int,input().split())
li = list(range(1,N+1))
ans = []
num = 0

while len(li) != 0 :
    num = (num+ (K-1))%len(li)
    ans.append(str(li.pop(num)))
print("<"+", ".join(ans)+">")