# 백준 3447번 버그왕
# BRONZE 1
# 알고리즘 분류 : 문자열, 파싱, 정규 표현식
import re
import sys
li = sys.stdin.readlines()
for i in li :
    while True :
        i = re.sub(r'BUG','',i)
        if 'BUG' not in i :
            break
    print(i,end='')