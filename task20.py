f=open(' import_this.txt','r')
str_str=[]
str_s=""
for i in f.readlines():
    str_str.append(i)
for i in str_str[::-1]:
    str_s+=i
print(str_s)

