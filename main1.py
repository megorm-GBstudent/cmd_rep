print('I am file 1')
#1
a = int(input('Введите данные'))
if a==6 or a==7:
 print('Да')
elif 1<=a<=5:
 print('Нет')
else:
 print('Таких дней нет')

#3
x = int(input('Введите данные'))
y = int(input('Введите данные'))
x!= '0' and y!='0'
if x>0 and y>0:
    print('1 четверть')
elif x<0 and y>0:
    print('2 четверть')
elif x<0 and y<0:
    print('3 четверть')
elif x>0 and y<0:
    print('4 четверть')
    
#4
s = int(input('Введите данные'))
if s==1:
    print('диапозон возможных координат: x>=0 and y>=0')
elif s==2:
    print('диапозон возможных координат: x<=0 and y>=0')
elif s==3:
    print('диапозон возможных координат: x<=0 and y<=0')
elif s==4:
    print('диапозон возможных координат: x>=0 and y<=0')
else:
    print('нет такой четверти')
    
   #5
 x1 = float(input('Введите данные'))
x2 = float(input('Введите данные'))
y1 = float(input('Введите данные'))
y2 = float(input('Введите данные'))
import math
d = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
print(d)
