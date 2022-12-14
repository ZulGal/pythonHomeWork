# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06
# n = int(input('Введите натуральное число: '))
# print ('n = ',n, '[',end =' ')
# sum = 0
# for i in range(n):
#     element = round((1+1/(i+1))**(i+1),2)
#     sum += element
#     print (element, end =' ')
# print (f'] Сумма = {sum}')    

n = int(input('Введите натуральное число: '))
sum_=sum(round((1+1/(i+1))**(i+1),2) for i in range(n))
print (f' Сумма = {sum_}')
