def Task26_1():
    file = open('../files/26_1.txt')
    string = file.readlines()
    params = {}
    values = []
    for i in range(len(string)):
        if i == 0:
            temp = string[i].split(' ')
            params = {
                'max': int(temp[0]),
                'count': int(temp[1])
            }
        else:
            values.append(int(string[i]))

    values = sorted(values)
    print(values)
    maxValueSumm = 0;
    maxValue = 0;
    counter = 0
    for value in values:
        if (maxValueSumm + int(value)) <= int(params['max']):
            maxValueSumm += int(value)
            maxValue = int(value)
            counter += 1
    maxValueSumm -= maxValue
    values = reversed(values)
    counter -= 1
    for value in values:
        if (maxValueSumm + int(value)) <= int(params['max']):
            maxValueSumm += int(value)
            maxValue = int(value)
            counter += 1
    print(counter, maxValue, maxValueSumm)

    def Task27_1():
        file = open('../files/27_1_B.txt')
        string = file.readlines()
        N = 0
        values = []
        for i in range(len(string)):
            if i == 0:
                N = string[i]
            else:
                values.append(int(string[i]))

        maxSumm = 0
        firstNum = 0
        secondNum = 0
        for i in range(len(values) - 1):
            for j in range(i + 1, len(values)):
                summ = values[i] + values[j]
                if (summ > maxSumm) and (summ % 120 == 0) and (values[i] > values[j]):
                    maxSumm = summ
                    firstNum = values[i]
                    secondNum = values[j]

        print(firstNum, secondNum, values)