# 백준 2671번 잠수함식별
# GOLD 5
# 알고리즘 분류 : 문자열, 정규 표현식
import re
pattern = re.compile('(100+1+|01)+')
a = input()
if pattern.fullmatch(a) :
    print('SUBMARINE')
else :
    print('NOISE')