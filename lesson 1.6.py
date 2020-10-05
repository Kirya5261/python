a = int(input())
b = int(input())
day = 0
while a < b:
    day += 1
    a += a * 0.1
print('на %d-й день спортсмен достиг результата - не менее %d км'%(day, b))