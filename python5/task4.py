# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# сжатие
path = r'in.txt'
with open(path,'w') as f:
    f.write('aaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbsssttttttv')
with open(path,'r') as f:
    s = f.readline()+' '

def count(x,j):
    n = 0
    while s[j] == x:
        j += 1
        n += 1
    return n    

result = ''
i = 0
find = s[i]
while i < len(s)-1:
    k = count(find,i)
    i += k
    result = result + str(k) + find
    find = s[i]
path=r'out.txt'
with open(path,'w') as f:
    f.write(result)

# восстановление
path = r'out.txt'     
with open(path,'r') as f:
    s = f.readline()
    
digit = ['0','1','2','3','4','5','6','7','8','9']

def number():
    a=[]
    i = 0
    while i<len(s):
            first_i = i
            while s[i] in digit:
                i += 1
            a.append(int(s[first_i:i]))
            a.append(s[i]) 
            i += 1
    return(a)
    
list_ = number()
result = ''
i = 0
while i < len(list_): 
    for j in range(list_[i]):
        result = result + list_[i+1] 
    i +=2

with open(path,'a') as f:
    f.write('\n')
    f.write(result)
