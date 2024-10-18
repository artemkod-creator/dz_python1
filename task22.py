f=open('dump.txt', encoding='utf-8')
kolvo_strok=0
for line in open('dump.txt', encoding='utf-8'): #проходися по каждой строке и считаем их количество
    kolvo_strok+=1
str_1=''
for i in range(kolvo_strok):
    str_1+=f.readline()
print("Количесто букв а: ",str_1.count('а'))
print("Количесто букв е: ",str_1.count('е'))
print("Количесто букв ё: ",str_1.count('ё'))
print("Количесто букв и: ",str_1.count('и'))
print("Количесто букв о: ",str_1.count('о'))
print("Количесто букв у: ",str_1.count('у'))
print("Количесто букв ы: ",str_1.count('ы'))
print("Количесто букв э: ",str_1.count('э'))
print("Количесто букв ю: ",str_1.count('ю'))
print("Количесто букв я: ",str_1.count('я'))