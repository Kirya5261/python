time = int(input('Введите количество секунд'))

hours = time // 3600
minutes = (time - hours*3600) // 60
seconds = (time - hours*3600 - minutes*60)
print("%.2i:%.2i:%.2i"%(hours, minutes, seconds))