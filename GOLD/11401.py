# 백준 11401번 이항 계수 3
# GOLD 1
# 알고리즘 분류 : 수학, 정수론, 조합론, 분할 정복을 이용한 거듭제곱, 모듈로 곱셈 역원, 페르마의 소정리
# 참고 : https://abcdefgh123123.tistory.com/350
N,K = map(int,input().split())
p = 1000000007
def fac(a) :
    res = 1
    for i in range(2,a+1) :
        res = res*i%p
    return res
def mul(A,B) :
    if B == 1 : return A%p
    m = mul(A,B//2)
    if B%2 : return(m*m*A)%p
    else : return (m*m)%p
print((fac(N)*(mul(fac(N-K)*fac(K),p-2)))%p)