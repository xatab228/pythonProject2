import itertools


# 18491 48
def Task18491():
    # Создаем словарь
    alph = ['0', 'Л', 'Ь', 'Г', 'А']

    # Создаем перестановки и определяем их как List
    # https://pythonworld.ru/moduli/modul-itertools.html
    allCombinations = list(itertools.permutations(alph))

    # Задаем дефолтное(стандартное) значение счетчика
    counter = 0

    # Создаем цикл, в котором пробегаемся по каждой комбинации
    for word in allCombinations:

        # Если первый символ слова это "Ь" то переходим к следующей итерации (следующему шагу) цикла
        if word[0] == 'Ь':
            continue
        isOkay = True

        # Создаем цикл, в котором пробегаемся по каждому символу слова
        for i in range(len(word)):

            # Проверка по условию,
            # Проверка (len(word) - 1 != i) для того чтобы проверить не вылезли ли мы за размер Листа
            if (word[i] == '0' or word[i] == 'А') and len(word) - 1 != i and word[i + 1] == 'Ь':
                isOkay = False
                break;
        if isOkay:
            counter += 1
    return counter


# 3208 РКРКО
def Task3208():
    # Создаем словарь
    alph2 = 'КОР'
    counter = 0
    # Создаем циклы (ровно столько сколько букв в итговом слове)
    # Каждый цикл бежит по словарю
    for s1 in alph2:
        for s2 in alph2:
            for s3 in alph2:
                for s4 in alph2:
                    for s5 in alph2:
                        counter += 1
                        answer = s1 + s2 + s3 + s4 + s5
                        if counter == 182:
                            return answer


print(Task3208())
