# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов 
# списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

a = [2, 3, 5, 9, 3]

# def odd_(n:int)->bool:
#     if n % 2 != 1:
#         return (0)
#     else:
#          return (1)  

# def sum_(x: list)->int:
#     s = 0 
#     for i in range(len(x)):
#         if odd_(i):
#             s += x[i]
#     return s
           
# print(sum_(a))      

s = sum(list(a[i] for i in  range(len(a)) if i%2 != 0 ))
print(s)

