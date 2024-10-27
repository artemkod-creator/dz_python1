import string
alphabet = list(string.ascii_lowercase)
list_chisel=[]
chisla=(input("Введите числа в строчку через пробел от 0 до 27: "))
chisla=chisla.split(' ')
print(chisla)
itog_str=''
for i in range(len(chisla)):
    if chisla[i].isdigit():
        int_chislo=int(chisla[i])
    else:
        continue
    for j in range(1):
         itog_str+=alphabet[int_chislo]
print(itog_str)
print(alphabet)
