# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
import string
znaki = string.punctuation

shifr="grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

alpa=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

spisok=[]

razgadka=" "
n=1
for n in range(1,20):
    for i in shifr:
        if i in znaki or i == " ":
            razgadka += i
            continue
        if alpa.index(i)+n>=25:
            razgadka+=alpa[alpa.index(i)+n-25]
            continue
        razgadka+=alpa[alpa.index(i)+n]
    print(razgadka,"\n")
    razgadka=" "