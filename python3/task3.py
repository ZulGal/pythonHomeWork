# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

a = [1.1, 1.2, 3.1, 10.01]
print(a)

def fractional_(x)->list:
    y = []
    for i in range(len(x)):
        y.append(round(x[i]%1,2)) 
    return y  

def minmax(x:list):
    min_ = 0
    max_ = 0 
    for i in range(len(x)-1):
        if x[i+1] < x[min_]:
            min_ = i+1
        if x[i+1] > x[max_]:
            max_ = i+1
    return min_,max_  

b = fractional_(a)
print(b)
c = minmax(b)
print(b[c[1]]-b[c[0]])



