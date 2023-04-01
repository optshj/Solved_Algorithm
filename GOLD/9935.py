# 백준 9935번 문자열 폭발
# GOLD 4
# 알고리즘 분류 : 자료 구조, 문자열, 스택
def sol() :
  A = list(input())
  B = list(input())
  li = []
  for i in range(len(A)) :
    li.append(A[i])
    if len(li) >= len(B) and li[-len(B):] == B:
      del li[-len(B):]
  print("".join(li) if li else "FRULA")
sol()