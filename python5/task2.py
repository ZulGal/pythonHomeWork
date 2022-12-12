# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая 
# ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты 
# у своего конкурента?
import random

total = 145
t = 145
total_step = 28
benefit = total % total_step

print("На столе 145 конфет. Играют два игрока делая ход друг после друга.") 
print("Первый ход определяется жеребьёвкой. За один ход можно забрать не более")
print("чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.")
print()
my_first = False
def lottery():
    global my_first
    print("Жеребьевка определит, кто первым ходит")
    user = int(input("Введите 0-если вы 'орел' и 1 -если вы 'решка': "))
    x = random.randint(0,1)
    if user == x:
        my_first = False
        print(f"Вы выбрали {user} и выпал {x}. 1-ход Ваш")
    else:
        my_first = True
        print(f"Вы выбрали {user} и выпал {x}. 1-ход мой")
    print()    

lottery()

def my_method(step):
    print(f"Мой ход: {step} Осталось  {t-step} конфет")

def user_method():
    global user_step
    user_step = int(input("Введите Ваш ход (от 1 до 27): "))
    while user_step not in range(1,28):
        user_step = int(input("Повторите Ваш ход : "))
    print(f"Ваш ход: {user_step} Осталось  {t-user_step} конфет")

def my_first_step_method():
    global my_step
    if user_step>benefit:
        my_step = total_step - user_step + benefit
    elif user_step == benefit:
        my_step = total_step - user_step
    else:
        my_step = benefit - user_step

def game():
    global total
    global t
    global benefit
    global total_step
    global user_step
    global my_step

    while t >= benefit:
        if t == total:
            if my_first:
                my_method(benefit)
                b = False
                t -= benefit
            else:
                user_method()
                b = True
                t -= user_step
                my_first_step_method()
                my_method(my_step)
                b = False
                t -=my_step
        else:
            if b:
                my_method(my_step)
                b = False
                t -= my_step
            else:
                user_method()
                b = True
                t -= user_step
                my_step = total_step - user_step
    if b == True:
        print("Вы сделали последний ход. Ваша победа!") 
    else:
        print("Последний ход мой. Победа - моя!")    
game()
