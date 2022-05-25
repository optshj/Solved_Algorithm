# 백준 1629번 곱셈
# SILVER 1
# 알고리즘 분류 : 수학, 분할 정복을 이용한 거듭제곱
# 메모리 30840KB, 시간 68ms ,언어 Python3 ,코드길이 : 170B
A,B,C = map(int,input().split())
def mul(A,B,C):
    if B == 1 : return A%C
    m = mul(A,B//2,C)
    if  B%2 : return(m*m*A)%C
    else : return(m*m)%C
print(mul(A,B,C))