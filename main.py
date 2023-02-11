import itertools
#18491 48
def searchAllCombinations():
    alph = ['0', 'Л', 'Ь', 'Г', 'А']
    allCombinations = list(itertools.permutations(alph))
    counter = 0
    for word in allCombinations:
        if word[0] == 'Ь':
            continue
        isOkay = True
        for i in range(len(word)):
            if (word[i] == '0' or word[i] == 'А') and len(word) - 1 != i and word[i + 1] == 'Ь':
                isOkay = False
                break;
        if isOkay:
            counter += 1
    return counter

print(searchAllCombinations())