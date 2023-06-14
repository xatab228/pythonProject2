def GetFile():
    file = open('files/17.txt')
    arr = []
    for num in file:
        arr.append(int(num))
    return arr

def Task_17():
    numberArray = GetFile()
    counter = 0
    difference = 0
    maxDifference = 0
    for i in range(len(numberArray)):
        for j in range(i + 1, len(numberArray)):
            first = numberArray[i]
            second = numberArray[j]
            difference = first - second
            if (difference % 60 == 0) and (first % 15 == 0 or second % 15 == 0):
                counter += 1
                if maxDifference < difference:
                    maxDifference = difference
                    difference = 0
    return [counter, maxDifference]
print(Task_17())