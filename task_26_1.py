def Task_26():
    file = open('FILES/26_1.txt')
    string = file.readlines()
    counterNum = 0
    counter = 0
    N = 0
    values = []
    maxCounter = 0
    for i in range(len(string)):
        if i == 0:
            N = string[i]
        else:
            values.append(int(string[i]))
    print(values)
    for i in range(len(values) - 1):
        for j in range(i + 1, len(values)):
            summ = values[i] + values[j]
            if (summ % 2 == 0) and (summ in values):
                counter = summ
                counterNum += 1
                if counter > maxCounter:
                    maxCounter = counter
    return([counterNum, maxCounter])
print(Task_26())