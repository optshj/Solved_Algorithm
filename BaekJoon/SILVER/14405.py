# 백준 14405번 피카츄
# SILVER 5
# 알고리즘 분류 : 문자열, 정규 표현식
word = input()
i = 0
while i < len(word):
    if word[i:i+2] == 'pi' :
        i += 2
    elif word[i:i+2] == 'ka' :
        i += 2
    elif word[i:i+3] == 'chu' :
        i += 3
    else :
        print('NO')
        exit()
print("YES")