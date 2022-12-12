# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая 
# ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты 
# у своего конкурента?
import random
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton

window = Tk()
window.title("Поиграем? ")
window.geometry('900x250')

l = Label(window, text="столе лежит 145 конфет.", font=("Arial Bold", 12)).grid(column = 0, row = 0)
l = Label(window, text="Жеребьевка определит, кто первым ходит").grid(column = 0, row = 1) 


def lottery():
    global my_first 
    l = Label(window, text="Жеребьевка !", font=("Arial Bold", 12)).grid(column = 0, row = 2)
    l = Label(window, text="Выбирайте, Вы - кто: орел или решка").grid(column = 0, row = 3)

    v =["орел ", "решка" ]
    c = Combobox(window, values = v)  
    c.current(0)    
    c.grid(column=0, row=4)
    print(c.get)
    def clicked():
        global my_first
        if v[x] == c.get():
            l = Label(window,text=f"{v[x]}! У вас - 1-ход!")
            l.grid(column=0, row=6)
            
            #user_step()
        else:
            l= Label(window,text=f"{v[x]}! 1-ход - у меня!")
            l.grid(column=0, row=6)
            my_first = True
            #my_step1(benefit)
        l = Label(window, text = "Нажмите на кнопку Игра")
        l.grid(column=0, row=7)

    def callbackFunc(event):
        l = Label(window, text=f"Вы выбрали {c.get()}, бросьте монетку, если выпадет {c.get()}, 1-ход - Ваш")
        l.grid(column=0, row=5)
        b = Button(window, text="Брось монетку", command=clicked)
        b.grid(column=1, row=5) 
    c.bind("<<ComboboxSelected>>", callbackFunc)

def my_method(step):
    #print(step)
    l = Label(window, text=f"Мой ход: {step}").grid(column = 2, row = 9)

def user_method():
    global user_step
    l = Label(window, text=f"Выберите ваш ход и нажмите Принять мой ход").grid(column = 0, row = 9) 
    n = [i for i in range(1,28)] 
    c = Combobox(window, values = n)   
    c.current(0)
    c.grid(column=0, row=10)
    def callbackFunc(event):
        global user_step
        user_step = int(c.get())
        print('?',user_step)
        l = Label(window, text=f"Ваш ход: {c.get()}").grid(column = 2, row = 8)
    c.bind("<<ComboboxSelected>>", callbackFunc)

def my_step_method():
    if user_step>benefit:
        my_step = total_step - user_step + benefit
    elif user_step == benefit:
        my_step = total_step - user_step
    else:
        my_step = benefit - user_step
        my_method(my_step)    
        t -= my_step       

def game():
    global total
    global t
    global benefit
    global total_step
    global user_step
    print(my_first, benefit,)
    while t != 0:
        if t == total:
            if my_first:
                my_method(benefit)
                t -= benefit
            else:
                user_method()
                t -= user_step
                print ('!',user_step,t)
                b = Button(window, text="Принять мой ход", command=my_step_method)
                b.grid(column=1, row=5)
                 
        else:
            user_method()
            t -= user_step
            my_step = total_step - user_step
            my_method(my_step)
            t -= my_step
        print('!!',t)
total = 145
t = 145
total_step = 28
benefit = total % total_step
user_step = 0

print(benefit)

x = random.randint(0,1)
x = 0 #!!!

my_first = False
b = Button(command = lottery,text ="Жеребьевка")
b.grid(column=0, row=2) 

b = Button(command = game,text ="Игра")
b.grid(column=3, row=7) 






 




# def my_step1(step):
#     lbl = Label(window, text=f"Мой ход: {step}").grid(column = 2, row = 9)
#     # t -= step
#     print(step)

# def user_step():
#     lbl = Label(window, text=f"Выберите ваш ход").grid(column = 0, row = 9) 
#     n = [i for i in range(1,28)] 
#     combo = Combobox(window, values = n)   
#     combo.current(0)
#     combo.grid(column=0, row=9)
    
#     def callbackFunc(event):
#         step = combo.get()
#         print(step)
#         lbl = Label(window, text=f"Ваш ход: {combo.get()}").grid(column = 2, row = 8)
       
#     combo.bind("<<ComboboxSelected>>", callbackFunc) 
    

# x = random.randint(0,1)
# x = 0
# def clicked():
#     if val[x] == combo.get():
#         lbl = Label(window,text=f"{val[x]}! У вас - 1-ход!")
#         lbl.grid(column=0, row=6)
#         user_step()
#     else:
#         lbl= Label(window,text=f"{val[x]}! 1-ход - у меня!")
#         lbl.grid(column=0, row=6)
#         my_step1(benefit)

# def callbackFunc(event):
#     lbl = Label(window, text=f"Вы выбрали {combo.get()}, бросьте монетку, если выпадет {combo.get()}, 1-ход - Ваш")
#     lbl.grid(column=0, row=5)
#     btn = Button(window, text="Брось монетку", command=clicked)
#     btn.grid(column=1, row=5) 

# combo.bind("<<ComboboxSelected>>", callbackFunc)

window.mainloop()





# import random
# from tkinter import *
# from tkinter.ttk import Combobox
# from tkinter.ttk import Checkbutton
# from tkinter.ttk import Radiobutton

# total = 145
# t = total
# n_step = 28
# benefit = total % n_step
# step: int(0)

# window = Tk()
# window.title("Поиграем? ")
# window.geometry('800x250')


# lbl = Label(window, text="столе лежит 145 конфет.", font=("Arial Bold", 12)).grid(column = 0, row = 0)
# lbl = Label(window, text="Жеребьевка определит, кто первым ходит").grid(column = 0, row = 1) 
 
# lbl = Label(window, text="Жеребьевка !", font=("Arial Bold", 12)).grid(column = 0, row = 2)
# lbl = Label(window, text="Выбирайте, Вы - кто: орел или решка").grid(column = 0, row = 3)

# val =["орел ", "решка" ]
# combo = Combobox(window, values = val)  
# combo.current(0)    
# combo.grid(column=0, row=4) 

# def my_step1(step):
#     lbl = Label(window, text=f"Мой ход: {step}").grid(column = 2, row = 9)
#     # t -= step
#     print(step)

# def user_step():
#     lbl = Label(window, text=f"Выберите ваш ход").grid(column = 0, row = 9) 
#     n = [i for i in range(1,28)] 
#     combo = Combobox(window, values = n)   
#     combo.current(0)
#     combo.grid(column=0, row=9)
    
#     def callbackFunc(event):
#         step = combo.get()
#         print(step)
#         lbl = Label(window, text=f"Ваш ход: {combo.get()}").grid(column = 2, row = 8)
       
#     combo.bind("<<ComboboxSelected>>", callbackFunc) 
    

# x = random.randint(0,1)
# x = 0
# def clicked():
#     if val[x] == combo.get():
#         lbl = Label(window,text=f"{val[x]}! У вас - 1-ход!")
#         lbl.grid(column=0, row=6)
#         user_step()
#     else:
#         lbl= Label(window,text=f"{val[x]}! 1-ход - у меня!")
#         lbl.grid(column=0, row=6)
#         my_step1(benefit)

# def callbackFunc(event):
#     lbl = Label(window, text=f"Вы выбрали {combo.get()}, бросьте монетку, если выпадет {combo.get()}, 1-ход - Ваш")
#     lbl.grid(column=0, row=5)
#     btn = Button(window, text="Брось монетку", command=clicked)
#     btn.grid(column=1, row=5) 

# combo.bind("<<ComboboxSelected>>", callbackFunc)

# window.mainloop()
