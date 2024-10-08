#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

spisok = []
for i in range(10):
    x=int(input("Введите число, которые хотите поместить в список: "))
    spisok.append(x)
spisok_new=[]
for value in range(len(spisok)):
    spisok_new.append(spisok[value]+1)
print(f"Ваш старый список {spisok}, и ваш новый список {spisok_new}")