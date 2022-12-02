# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = 45
print(n)

def decimal_to_binary_(x: int)->int:
    temp = 1
    while x !=0:
        temp = temp*10 + x%2
        x = x//2
    x = temp
    temp = 0
    while x != 0:
        temp = temp*10 +x%10
        x = x//10
    temp = temp //10
    return temp

print(decimal_to_binary_(n))
