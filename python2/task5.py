# Реализуйте алгоритм перемешивания списка.
import random
a = [1,2,3,4,5,6]
print(a)
for i in range(len(a)):
    k = random.randint(0,len(a)-1)
    m = random.randint(0,len(a)-1)
    temp = a[k]
    a[k] = a[m]
    a[m] = temp
print(a)    
