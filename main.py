def getFile(fileName):
    file = open(f'files/{fileName}.txt')
    arr = [];
    for num in file:
        arr.append(int(num))
    return arr


def Task40733():
    # Получаем привычный массив(лист) с числами из файла
    numberArray = getFile('40733');

    # Считаем количество четных элементов, а также их сумму и среднее значение
    allChetSumm = 0
    countChetSumm = 0
    for num in numberArray:
        if num % 2 == 0:
            countChetSumm += 1
            allChetSumm += num
    srChetSum = allChetSumm / countChetSumm

    # Приступаем к основному условию
    count = 0
    maxSummOfPair = 0

    for i in range(len(numberArray) - 1):
        firstNumberOfPair = numberArray[i]
        secondNumberOfPair = numberArray[i + 1]

        # Находим сумму, а также вводим две переменные в которые записываем наши условия( деление на 3 , а также сумма меньше среднего знначения суммы элементов)
        summ = firstNumberOfPair + secondNumberOfPair
        isDelOnThree = firstNumberOfPair % 3 == 0 or secondNumberOfPair % 3 == 0;
        isLessThenSumm = firstNumberOfPair < srChetSum or secondNumberOfPair < srChetSum

        # Выполняем проверку, если все ок то в счетчик прибавляем единицу, а также не забываем про нахождение максимального элемента
        if isDelOnThree and isLessThenSumm:
            count += 1
            if summ > maxSummOfPair:
                maxSummOfPair = summ

    # Вывод массивом (*для удобства)
    return [count, maxSummOfPair]

print(Task40733())