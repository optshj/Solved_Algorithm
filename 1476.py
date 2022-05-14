#1476번 날짜 계산
#SILVER 5
E,S,M = map(int,input().split())
result = 1
E %= 15
S %= 28
M %= 19
while True :
    if result%15 == E and result%28 == S and result%19 == M :
        break
    else :
        result += 1
print(result)