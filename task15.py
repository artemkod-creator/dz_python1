from random import randint as ri

words = ["оператор", "конструкция", "объект"]
desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования.",
           "Это синтаксическая структура, которая определяет способ организации кода.",
           "Это сущность, представляющая собой экземпляр класса." ]

word_index = ri(0, len(words) - 1)
word_for_play = words[word_index]
player_word = [" ▒"] * len(word_for_play)
attempt = 0
print("Угадайте слово по подсказке: " + desc_[word_index] + "\n")
print("".join(player_word))

while 0 <= attempt < 10 and " ▒" in player_word:
    letter = input(f"\nУ вас осталось {10 - attempt} попыток! \nВведите букву: ")
    if letter in word_for_play:
        start = 0
        for j in range(word_for_play.count(letter)):
             indx = word_for_play.index(letter, start)
             player_word[indx] = " " + letter
             start = indx + 1
        print("".join(player_word))
    else:
        print("Такой буквы в слове нет!")
    attempt += 1
else:
    if " ▒" in player_word:
        print("Увы, слово отгадать Вам не удалось!")
    else:
        print("Поздравляем, Вы угадали слово!")
