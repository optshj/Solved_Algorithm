# 백준 1918번 후위 표기식
# GOLD 2
# 알고리즘 분류 : 자료 구조, 스택
# 2학년 1학기 자료 구조 과제 1번 문제
li = input()
stack = []
ans = ""
pri = {'+':0,'-':0,'*':1,'/':1,'(':-1}
for i in li :
    if "A" <= i <= "Z" :
        ans += i
    elif i == "(" :
        stack.append(i)
    elif i == ")" :
        while stack[-1] != "(" :
            ans += stack.pop()
        stack.pop()
    else :
        while stack and pri[stack[-1]] >= pri[i] :
            ans += stack.pop()
        stack.append(i)
while stack :
    ans += stack.pop()
print(ans)