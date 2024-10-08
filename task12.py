#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)

while True:
    massa_tela = int(input("Введите массу тела: "))
    ed_massa = int(input("Введите число от 1 до 5, где  1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер, 6 - выйти из программы : "))
    match ed_massa:
        case 1:
            print(f"{massa_tela} кг")
        case 2:
            print(f"{massa_tela // 1000000} кг")
        case 3:
            print(f"{massa_tela // 1000} кг")
        case 4:
            print(f"{massa_tela * 1000} кг")
        case 5:
            print(f"{massa_tela * 100} кг")
        case 6:
            break
