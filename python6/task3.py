# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной 
# строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

# n = int(input('Введите натуральное число '))
# a = []
# for i in range(-n,n+1):
#     a.append(i)
# print(a) 

# s = input('Введите индексы элементов ')
# index = []
# for i in range(len(s)):
#     if s[i] != ' ':
#         index.append(int(s[i]))

# mult = 1
# for i in range(len(index)):
#     mult *= a[index[i]]
# print(mult)

n = int(input('Введите натуральное число '))
a = [i for i in range(-n,n+1)]
print(a)

index = list(map(int,input('Введите индексы элементов ').split()))
print(index)

mult = 1
for i in range(len(index)):
    mult *= a[index[i]]
print(mult)


