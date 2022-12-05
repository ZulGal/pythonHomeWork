# Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N
a = int(input('Введите натуральное число '))

def simple_(x:int)->bool:
    for i in range(2,x//2+1):
        if x%i == 0:
            return 0
    return 1
b = []
if simple_(a):
    b = [1]
for i in range(2,a+1):
    if simple_(i) and a%i == 0:
        b.append(i)
print(b)        

