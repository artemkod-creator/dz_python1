users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]
sortirovka=int(input("Выберите число для сортировки, где\n1. По возрасту\n"
                     "2. По первой букве\n"
                     "3. По группе\n "
                     "Вводите тут : "))
match sortirovka:
    case 1:
        age_=int(input("Введите возраст: "))
        n=0
        while n<len(users):
            dict_ = users[n].get('age')
            if age_<dict_:
                print(users[n])
            n+=1
    case 2:
        name_=(input("Введите первую букву пользователя: "))
        n=0
        while n<len(users):
            dict_ = users[n].get('login')
            if dict_[0]==name_:
                print(users[n])
            n+=1
    case 3:
        group_=(input("Введите группу: "))
        n=0
        while n<len(users):
            dict_=users[n].get('group')
            if group_==dict_:
                print(users[n])
            n+=1


