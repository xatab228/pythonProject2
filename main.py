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



# print(f"sasd {task14()}")

# Работает только в том случае, если число представленно в 10 системе счисления
def TenToSS(num, ss):
    answer = '';
    while num != 0:
        answer += str(num % ss);
        num = num // ss;
    return answer[::-1]

def Task33484():
    summ = pow(343, 6) - pow(7, 10) + 47;
    sumInSevenSS = TenToSS(summ, 7)
    return sumInSevenSS.count('6')

print(Task33484())