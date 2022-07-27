# 백준 2864번 5와 6의 차이
# BRONZE 2
# 알고리즘 분류 : 수학, 그리디 알고리즘, 사칙연산
a,b = map(str,input().split())
max_val = int(a.replace("5","6")) + int(b.replace("5","6"))
min_val = int(a.replace("6","5")) + int(b.replace("6","5"))
print(min_val,max_val)