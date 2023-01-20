def taskWithBinaryCode(limit):
    isComplete = True
    num = 2
    while isComplete:
        # Transform to binary and delete '0b'

        binaryNumber = str(bin(num)[2:])

        # First Variant

        # [startPosition:endPosition:step] work only with String and List type !!!
        # Defaults:
        # startPosition = 0
        # endPosition = len(LIST)
        # step = 1

        # index: 0 1 2 3 4 5 6 7
        # value: 1 0 1 0 0 0 1 0 => binaryNumber

        # К.с.м: 1 2 3 4 5 6 7 8
        # value: 1 0 1 0 0 0 1 0 => binaryNumber

        # nullNumberCount = binaryNumber[::2].count('0')
        # oneNumberCount = binaryNumber[1::2].count('1')

        # Second Variant

        oneNumberCount = 0
        nullNumberCount = 0
        for i in range(len(binaryNumber)):
            if ( i % 2 != 0 and binaryNumber[i] == '1'):
                oneNumberCount += 1
            if ( i % 2 == 0 and binaryNumber[i] == '0'):
                nullNumberCount += 1
        modul = abs(oneNumberCount - nullNumberCount)
        if modul == limit:
            isComplete = False
        else:
            num += 1
    return num


def taskWithNewNumber(searchValue):
    isComplete = True
    num = 10000
    while num < 100000 and isComplete:
        temp = str(num)
        subNumFirst = int(temp[0]) + int(temp[2]) + int(temp[4])
        subNumSecond = int(temp[1]) + int(temp[3])
        maxNumber = str(max(subNumFirst, subNumSecond))
        minNumber = str(min(subNumFirst, subNumSecond))
        summary = minNumber + maxNumber
        if int(summary) == searchValue:
            isComplete = False
        else:
            num += 1
    return num


# print(taskWithNewNumber(621))


print(taskWithBinaryCode(5))