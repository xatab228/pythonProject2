def Perevod(ss, num):
    answer = ''
    while num != 0:
        answer += str(num% ss)
        num = num // ss
    return answer[::-1]

num = 5 ** 36 + 5 ** 24 -25
fifthNum = Perevod(5, num)
counter = fifthNum.count('4')
print(counter)
