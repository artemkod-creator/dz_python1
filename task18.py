f=open('hello..txt','w+t')
f.write('Hello')
f.seek(0)
print(f.read())
f.close()

