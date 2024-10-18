# # todo: База данных пользователя.
# # Задан массив объектов пользователя
#
#
# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]
#
# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.
#
# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1
#
# #Затем сообщение для ввода
# Ввидите критерии поиска: 16
#
# Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"

def age(users):
    global man_age
    for i in range(len(users)):
        man_age.append(users[i].get('age'))
    return sorted(man_age,reverse=True)

def name(users):
    global man_name
    for i in range(len(users)):
        man_name.append(users[i].get('login'))
    return sorted(man_name,reverse=True)

def group(users):
    global man_group
    for i in range(len(users)):
        man_group.append(users[i].get('group'))
    return sorted(man_group)

man_age=[]
man_name=[]
man_group=[]

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

sortirovka=int(input("Ввведите число от 1 до 3, чтобы отсортировать список "
                     " 1. По возрасту "
                     " 2. По первой букве имени "
                     " 3. По группе: "))

# if sortirovka==1:
#     man_age=man_age.sort()
print(age(users))
print(name(users))
print(group(users))
