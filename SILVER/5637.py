# 백준 5637번 가장 긴 단어
# SILVER 4
# 알고리즘 분류 : 문자열, 파싱, 정규 표현식
# 파이썬 re 라이브러리를 활용
import re
li = []
while True :
    li.extend(input().split())
    if li[-1] == 'E-N-D' :
        break
ans = []
for i in li :
    ans.append(re.sub('[^a-z-]','',i.lower()))
ans.sort(key = lambda x: len(x),reverse= True)
print(ans[0])