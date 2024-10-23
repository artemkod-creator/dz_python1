f=open(' import_this.txt','r')
str_s=""
for i in f.readlines()[::-1]:
    str_s+=i
print(str_s)
