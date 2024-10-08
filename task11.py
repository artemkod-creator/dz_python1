
while True:
    year = int(input("Введите год:"))
    if 1 < year < 1000:
        if year%10==1:
             stoletie = year // 10 +1
        else:
            stoletie = year // 100
        print(f"В {year} году было {stoletie} столетие")
    elif 1000 < year < 10000:
        if year%10==1:
            stoletie = year // 100 +1
        else:
            stoletie = year // 100
        print(f"В {year} году было {stoletie} столетие")
    elif year < 0:
        exit("Вы ввели отцриательное число")
