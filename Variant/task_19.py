def game(hip, step):
    if (step == 2 or step == 4) and (hip >= 39): return True
    elif (step < 4) and (hip >= 39): return False
    elif (step == 4) and(hip < 39): return False
    else:
        if step % 2 == 1:
            return (
                game(hip + 1, step + 1)
                or
                game(hip + 2, step + 1)
                or
                game(hip * 2, step + 1)
            )
        else:
            return (
                game(hip + 1, step + 1)
                and
                game(hip + 2, step + 1)
                and
                game(hip * 2, step + 1)
            )
def game1(hip, step):
    if (step == 2) and (hip >= 39): return True
    elif (step < 2) and (hip >= 39): return False
    elif (step == 2) and(hip < 39): return False
    else:
        if step % 2 == 1:
            return (
                game1(hip + 1, step + 1)
                or
                game1(hip + 2, step + 1)
                or
                game1(hip * 2, step + 1)
            )
        else:
            return (
                game1(hip + 1, step + 1)
                and
                game1(hip + 2, step + 1)
                and
                game1(hip * 2, step + 1)
            )
for s in range(1,39):
    if game(s, 0) == True and game1(s, 0) == False:
        print(s)