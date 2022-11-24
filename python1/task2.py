# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Z⋁ Y ) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат. 
# ⋀ - and ⋁ - or ¬ - not

a = [False,True]
for x in a:
    for y in a:
        for z in a:
            print (f'¬({x}⋁{z}⋁{y} = ¬{x}⋀¬{y}⋀¬{z}     {not(x or z or y)} = {not x and not y and not z}') 
print()
for x in range(2):
    for y in range(2):
        for z in range(2):
            print (f'¬({x}⋁{z}⋁{y} = ¬{x}⋀¬{y}⋀¬{z}     {not(x or z or y)} = {not x and not y and not z}') 