# 백준 1076번 저항
# BRONZE 2
# 알고리즘 분류 : 구현
val = {"black" : 0 ,"brown" : 1, "red" : 2, "orange" : 3, "yellow" : 4,"green" : 5, "blue" : 6,"violet" : 7,"grey" : 8, "white" : 9}
print((val[input()]*10 + val[input()])*10**val[input()])