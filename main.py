
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
    game = gameData(64, 4);
    countSpace = 32
    for step in game:
        print(int(countSpace) * ' ' + str(step))
        countSpace -= len(step) * 2



StoneTask()
