def taskWithBinaryCode(limit):
    isComplete = True;
    num = 2
    while isComplete:
        # Transform to binary and delete '0b'

        binaryNumber = str(bin(num)[2:])

        # First Variant

        oneNumberCount = binaryNumber[::2].count('0')
        nullNumberCount = binaryNumber[1::2].count('1')

        # Second Variant

        # oneNumberCount = 0
        # nullNumberCount = 0
        # for i in range(len(binaryNumber)):
        #     if ( i % 2 != 0 and binaryNumber[i] == '1'):
        #         oneNumberCount += 1
        #     if ( i % 2 == 0 and binaryNumber[i] == '0'):
        #         nullNumberCount += 1

        modul = abs(oneNumberCount - nullNumberCount)
        if modul == limit:
            isComplete = False
        else:
            num += 1
    return num


def taskWithNewNumber(searchValue):
    isComplete = True;
    num = 10000
    while num < 100000 and isComplete:
        temp = str(num)
        subNumFirst = int(temp[0]) + int(temp[2]) + int(temp[4])
        subNumSecond = int(temp[1]) + int(temp[3])
        summary = str(subNumSecond) + str(subNumFirst)
        if int(summary) == searchValue:
            isComplete = False
        else:
            num += 1
    return num


print(taskWithBinaryCode(5))
print(taskWithNewNumber(621))
