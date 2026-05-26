classes = []

with open('en-ru.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line == '':
            continue

        parts = line.split(' - ')
        english_word = parts[0]
        russian_part = parts[1]

        russian_words = russian_part.split(', ')

        for rus_word in russian_words:
            pairs.append([rus_word, english_word])

classes.sort()

with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for pair in classes:
        line = pair[0] + ' – ' + pair[1] + '\n'
        file.write(line)

print('Готово!')