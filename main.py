

def Task34539():
    P = list(range(22, 73))
    Q = list(range(42, 102))
    A = []
    for x in range(0, 110):
        if not (not (not (x in A) and (x in P)) or (x in Q)):
            A.append(x)
    return A;



def Del(n,m):
    return n % m == 0
def Task35904():
    answer = 0
    for A in range(1, 10000):
        isComplete = True
        for x in range(1, 10000):
            if (Del(A, 40) and (Del(780, x) <= ((not(Del(A, x))) <= (not(Del(180, x)))))) == False:
                isComplete = False
                break;
        if isComplete:
            answer = A
            break

    return answer;


def Task35989():
    answer = 0
    for A in range(1, 10000):
        isComplete = True
        for x in range(1, 10000):
            if ((x & 73 == 0) <= ((x & 28 != 0) <= (x & A != 0))) == False:
                isComplete = False
                break;
        if isComplete:
            answer = A
            break

    return answer;


def Task19067():
    answer = 0
    for A in range(1, 1000):
        isComplete = True
        for x in range(1, 1000):
            for y in range(1, 1000):
                if ((x + 2 * y < A) or (y > x) or (x > 30)) == False:
                    isComplete = False
                    break;
            if isComplete == False:
                break
        if isComplete:
            answer = A
            break
    return answer;

def Task9653():
    P = list(range(10, 29))
    Q = list(range(13, 18))
    A = list(range(1, 50))
    for x in range(1, 50):
        if not (((x in A) <= (x in P)) or (x in Q)):
            A.remove(x)
    return A;
print(Task9653())
# answer 41 - 22 + 1 = 20
# print(Task34539())

# answer 120
# print(Task35904())

# answer 20
# print(Task35989())

# answer 91
# print(Task19067())