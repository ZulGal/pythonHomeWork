# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

s = 'Я люблю Джавуабв иабв Питон'
l = ' '.join(list(filter (lambda x: not('абв'in x), s.split())))
print(l)
print(' '.join((i for i in s.split() if 'абв' not in i))) 