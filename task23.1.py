import string

shifr = open('shifr1.txt', 'rt', encoding='utf-8')

alpha = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

znaki = string.punctuation

cesar = ""

count = 1

for line in shifr:
    for i in line:
        if i.lower() in znaki or i == " ":
            cesar += i
            continue
        if i.lower() == '\n':
            cesar+='\n'
        if i.lower() in alpha:  #
            new_index = (alpha.index(i.lower()) + count) % len(alpha)
            new_char = alpha[new_index]
            if i.isupper():
                new_char = new_char.upper()
            cesar += new_char
        else:
            cesar += i
    count += 1

shifr.close()
print(cesar)