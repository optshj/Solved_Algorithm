#1330번 두 수 비교하기
#BRONZE 4
a,b = map(int,input().split())
if a > b :
    print('>')
elif a < b :
    print('<')
else :
    print('==')