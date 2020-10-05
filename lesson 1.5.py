proceeds = int(input('введите выручка'))
damages = int(input('введите издержки'))
if profit - damages > 0:
    print('прибыль')
    print('рентабельность: %.1f'%(((proceeds-damages)/proceeds)*100) + "%")
    count = int(input('введите количество сотрудников'))
    print('прибыль в расчетет на одного сотрудника: %f'%((proceeds-damages)/count))
else: print('убытки')