#2447¹ø º° Âï±â - 10
#SILVER 1
import sys
def star(a):
    if a == 3 :
        star_li = ['***','* *','***']
        return star_li
    else :
        m_star = star(a//3)
        star_li = []
        for i in m_star:
            star_li.append(i*3)
        for i in m_star:
            star_li.append(i+' '*(a//3)+i)
        for i in m_star:
            star_li.append(i*3)
            
        return star_li



a = int(sys.stdin.readline())
print('\n'.join(star(a)))