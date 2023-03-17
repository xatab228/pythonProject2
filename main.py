# https://inf-ege.sdamgia.ru/problem?id=48391
def task14():
    #12 SS - 0123456789AB
    #14 SS - 0123456789ABCD
    twelve = '0123456789AB'
    completed = []
    for x in twelve:
        for y in twelve:
            twelveDigit = y + 'AA' + x
            fourthDigit = x + '02' + y
            tenTwelveDigit = int(twelveDigit, 12)
            tenFourthDigit = int(fourthDigit, 14)
            summary = tenTwelveDigit + tenFourthDigit
            if summary % 80 == 0:
                completed.append(summary)
    print(completed)
    return min(completed) // 80



print(task14())