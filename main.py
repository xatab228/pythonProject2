
def gameData(stones, stepsCount):
    stepsData = []
    for step in range(stepsCount):
        if step == 0:
            stepsData.append([stones + 1, stones * 2])
        else:
            stepData = stepsData[step - 1]
            newStep = []
            for stoneIndex in range(len(stepData)):
                newStep.append(stepData[stoneIndex] + 1)
                newStep.append(stepData[stoneIndex] * 2)
            stepsData.append(newStep)
    return stepsData


def StoneTask():
    defaultStonesCount = 2;
    defaultStepsCount = 2;
    game = gameData(defaultStonesCount, defaultStepsCount);

    #ONLY PRINT
    stepsCount = 1
    countSpace = 32
    print('S' + int(countSpace + 6) * ' ' + str(defaultStonesCount))
    for step in game:
        if stepsCount % 2 == 0:
            name = 'Ваня'
        else:
            name = 'Петя'
        print(name + int(countSpace) * ' ' + str(step))
        countSpace -= len(step) * 2
        stepsCount += 1


# 19 - 64
# 20 - 32, 63
# 21 - 62
StoneTask()
