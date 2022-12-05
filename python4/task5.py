# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов 
# (складываются числа, у которых "х" в одинаковых степенях).
s1 = ''
s2 = ''
path1 = r't1.txt'
with open(path1,'w') as f1:
    f1.write('5*(x**3) + 13*(x**2) + 9*x + 2 = 0')
path2 = r't2.txt'
with open(path2,'w') as f2:
    f2.write('2*(x**4) + 70*(x**2) + 2 = 0')

with open(path1,'r') as f1:  
    s1 = f1.readline().split('+') 
with open(path2,'r') as f2:  
    s2 = f2.readline().split('+') 

def create_list(s):
    l = []
    for i in range(len(s)):
        k = s[i].find('*')
        if k == -1:
            k = s[i].find('=')
            mono = ''
            coef= int(s[i][0:k-1])
        else:
            if s[i][k+1] == ' ':
                mono= '*x'
                coef = int(s[i][1:k])
            else:
                mono= s[i][k:len(s[i])-1]
                coef= int(s[i][0:k])
        l.append([coef,mono])
    return l
l1 = create_list(s1)   
l2 = create_list(s2)     
i = 0
j = 0  
s =''  
while i < len(l1):
    while j < len(l2):
        if l1[i][1] == l2[j][1]:
            mono = l1[i][1]
            coef = str(l1[i][0] + l2[j][0])
            s = s+' + '+ (coef+mono)  
            i += 1
            j += 1
        elif l1[i][1] > l2[j][1]:
            while l1[i][1] > l2[j][1]:
                mono = l1[i][1]
                coef = str(l1[i][0])
                s = s+' + '+ (coef+mono)  
                i += 1
        else:
            while l1[i][1] < l2[j][1]:
                mono = l2[j][1]
                coef = str(l2[j][0]) 
                j +=1
                s = s+' + '+ (coef+mono)
path3 = r't3.txt'
with open(path3,'w') as f3:
    f3.write(s[3:])                







