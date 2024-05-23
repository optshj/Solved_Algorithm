# 백준 1013번 Contact
# GOLD 5
# 알고리즘 분류 : 문자열, 정규 표현식
import sys
import re
pattern = re.compile('(100+1+|01)+')
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    li = sys.stdin.readline().rstrip()
    if pattern.fullmatch(li) :
        print('YES')
    else :
        print('NO')