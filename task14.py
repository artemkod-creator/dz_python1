spisok=[]
dlina_spiska=int(input("Введите длину списка: "))
for i in range(dlina_spiska):
    chislo=int(input("Введите значения списка через enter: "))
    spisok.append(chislo)
for i in range(len(spisok)):
    for j in range(i+1,len(spisok)):
        if spisok[i]==spisok[j]:
            print(f"Для числа {spisok[i]} минимальное растояние в массиве по индексам: {spisok.index(spisok[i])}"
                  f" и {spisok.index(spisok[j],spisok[i])}")