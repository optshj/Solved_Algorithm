# 백준 2816번 디지털 티비
# BRONZE 1
# 알고리즘 분류 : 구현, 구성적
N = int(input())
ans = ''
li = [input() for _ in range(N)]
idx_1 = li.index('KBS1')
idx_2 = li.index('KBS2')
ans += '1'*idx_1
ans += '4'*idx_1
if idx_1 > idx_2 :
    ans += '1'*(idx_2+1)
    ans += '4'*(idx_2)
else :
    ans += '1'*(idx_2)
    ans += '4'*(idx_2-1)
print(ans)