#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
#
# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
#
#
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

razmer_mass=int(input("Введите размер массива: "))
massiv=[]
for value in range(razmer_mass):
    x=int(input("Введите значение, которые хотите поместить в массив: "))
    massiv.append(x)
print(massiv)
for value_1 in range(len(massiv)):
    for value_2 in range(value_1+1,len(massiv)):
        if massiv[value_1]==massiv[value_2]:
            print(massiv.index(value_1+1),massiv.index(value_2)+1)

list_1=list(eval(input()))
print(list_1)
list_2=list(eval(input()))
print(list_2)
extened_list=list_1+list_2
count=len(extened_list)
print(extened_list.append(count))
