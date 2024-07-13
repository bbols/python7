import os

f = open('text.txt','w',encoding='utf-8')
f.write('fadasd')
f.close()

file =open('text.txt','r',encoding='utf-8')
print(file.read())
file.close()

file 