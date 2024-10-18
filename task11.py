year=int(input("Введите год: "))
if year<=100:
      print(f"В {year} году было 1 столетие")
      exit(0)
if int(year)%10 + int(year)%100==0:
    stoletie=year//100
    print(f"В {year} году было {stoletie} столетие")
else:
    stoletie = year//100+1
    print(f"В {year} году было {stoletie} столетие")

