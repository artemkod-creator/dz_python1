# todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.
# Пример:
# x = 10
# y = 15
# z = 2
# Ответ:
# Наибольшее число 15

x=int(input("Введите значение X: "))
y=int(input("Введите значение Y: "))
z=int(input("Введите значение Z: "))
if x>y and x>z:
    print(f"Наибольшее число {x}")
elif y>x and y>z:
    print(f"Наибольшее число {y}")
elif z>x and z>y:
    print(f"Наибольшее число {z}")
else:
    print("Нет наибольшего числа")