def Task_8():
    alph = 'А', 'О', 'У'
    counter = 0
    result = 0
    for s1 in alph:
        for s2 in alph:
            for s3 in alph:
                for s4 in alph:
                    for s5 in alph:
                        answer = s1 + s2 + s3 + s4 + s5
                        counter += 1
                        if counter == 125:
                            result = answer
    return result
print(Task_8())