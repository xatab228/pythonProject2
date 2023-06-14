def Task_5():
    n = 105
    counterZero = 0
    counterOne = 0
    isCompleted = True
    while isCompleted == True:
        binNum = str(bin(n)[2:])
        counterOne = binNum.count('1')
        counterZero = binNum.count('0')
        if counterOne == counterZero:
            binNum = binNum + binNum[-1]
        elif counterOne > counterZero:
            binNum = binNum + '0'
        elif counterOne < counterZero:
            binNum = binNum + '1'
        counterOne = binNum.count('1')
        counterZero = binNum.count('0')
        if counterOne == counterZero:
            binNum = binNum + binNum[-1]
        elif counterOne > counterZero:
            binNum = binNum + '0'
        elif counterOne < counterZero:
            binNum = binNum + '1'
        counterOne = binNum.count('1')
        counterZero = binNum.count('0')
        if counterOne == counterZero:
            binNum = binNum + binNum[-1]
        elif counterOne > counterZero:
            binNum = binNum + '0'
        elif counterOne < counterZero:
            binNum = binNum + '1'
        answer = int(binNum,2)
        if answer % 4 == 0:
            result = n
            isCompleted = False
        else:
            n += 1
    return result
print(Task_5())