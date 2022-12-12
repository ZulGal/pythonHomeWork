# Создайте программу для игры в ""Крестики-нолики"".
import random
s = [
    ['-','-','-','-','-','-','-','-','-','-','-','-','-'],
    ['|',' 1 ','|',' 2 ','|',' 3 ','|'],
    ['-','-','-','-','-','-','-','-','-','-','-','-','-'],
    ['|',' 4 ','|',' 5 ','|',' 6 ','|'],
    ['-','-','-','-','-','-','-','-','-','-','-','-','-'],
    ['|',' 7 ','|',' 8 ','|',' 9 ','|'],
    ['-','-','-','-','-','-','-','-','-','-','-','-','-'],
    ]
ind = {1:(1,1),2:(1,3),3:(1,5),
       4:(3,1),5:(3,3),6:(3,5), 
       7:(5,1),8:(5,3),9:(5,5)
       }

list_of_steps = [1,2,3,4,5,6,7,8,9]       

def field():
    for i in range(len(s)):
        row_ = ''
        for j in range(len(s[i])):
            row_ = row_+ s[i][j]
        print(row_)
def user_method():
    global my_que
    user_step = int(input("Введите № клетки (от 1 до 9): "))
    while user_step not in list_of_steps:
        user_step = int(input("Повторите Ваш ход : "))
    s[ind[user_step][0]][ind[user_step][1]] = ' O '
    field()
    my_que = True
    list_of_steps.remove(user_step)

def my_method():
    global my_que
    i = random.randint(0,len(list_of_steps)-1)
    my_step = list_of_steps[i]
    print(f'Мой ход: {my_step}')
    s[ind[my_step][0]][ind[my_step][1]] = ' X '
    field()
    my_que = False
    list_of_steps.remove(my_step)

field()
win = False
my_que = False
while (len(list_of_steps) != 0)and (win != True):
    if my_que:
        my_method()
    else:    
        user_method()
    if s[1][1] == s[1][3] == s[1][5] or s[3][1] == s[3][3] == s[3][5]or s[5][1] == s[5][3] == s[5][5]:
        win = True
    if s[1][1] == s[3][1] == s[5][1] or s[1][3] == s[3][3] == s[5][3]or s[1][5] == s[3][5] == s[5][5]:
        win = True
    if s[1][1] == s[3][3] == s[5][5] or s[1][5] == s[3][3] == s[5][1]:
        win = True
    # print(s[1][1] == s[1][3] == s[1][5])
print('Победа!!!')    