x=input("Введите значение x: ")
print("x = ", x)
y=input("Введите значение y: ")
print("y = ", y)
import math
a=int(x)**(int(y)/int(x))-(int(y)/int(x))**(1/3)
psi=abs(a)+(int(y)-int(x))
print("Ответ: ", psi)