# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
#random.randint(0,len(a)-1)
from random import randint
n = 4
list_=[]
for i in range(n+1):
    list_.append(randint(0,9))

def polinom_(k, a):
    s = ''
    for i in range(k):
        if a[i] != 0:
            if i <= k-2:
                if s == '':
                    s = s + f'{a[i]}*(x**{2*k-k-i})'
                else:
                     s = s + f' + {a[i]}*(x**{2*k-k-i})'   
            elif i == k-1:
                if s == '':
                    s = s + f'{a[i]}*x'
                else:    
                    s = s + f' + {a[i]}*x'
    if a[k] !=0: 
        if s == '':
            s = s + f'Это не многочлен: {a[i+1]}' 
        else:
            s = s + f' + {a[i+1]}'
    s = s + f' = 0' 
    return(s)
p = polinom_(n,list_)
path_ = r'text.txt'
with open(path_,'w') as f:
    f.write(polinom_(n,list_))  