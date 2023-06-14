def Task_15():
    answer = []
    for A in range(1, 100):
        isCompleted = True
        for x in range(0,100):
            if ((x & A != 0) <= ((x & 10 == 0) <= (x & 3 != 0))) == False:
                isCompleted = False
        if isCompleted == True:
            answer.append(A)
    return answer
print(Task_15())
