
def Tree(start,end):
    stepsData = []
    maxSteps = end - start

    for step in range(maxSteps):
        if step == 0:
            stepsData.append([start + 1,start + 2,start * 3])
        else:
            stepData = stepsData[step - 1]
            newStep = []
            for number in stepData:
                newStep.append(number + 1)
                newStep.append(number + 2)
                newStep.append(number * 3)
            stepsData.append(newStep)
    return stepsData


def Task23():
    return Tree(2,15)



print(Task23())