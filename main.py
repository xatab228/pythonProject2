
def Task24_1():
    file = open('../files/24_1.txt')
    string = file.readline()
    temp = {}
    for i in range(0, len(string) - 2):
        if string[i] == string[i + 1]:
            if temp.get(string[i + 2]) != None:
                temp[string[i + 2]] += 1
            else:
                temp[string[i + 2]] = 0
    print(temp, max(temp, key=temp.get))

def Task24_2():
    file = open('../files/24_2.txt')
    lines = file.readlines();
    counter = 0
    for line in lines:
        if line.count('A') > line.count('E'):
            counter += 1
    print(counter)

def Task25_1():
    for x in range(1049341, 1949399941):
        string = str(x)
        if string[0] == '1' and string[2:5] == '493' and string[-2] == '4' and string[-1] == '1':
            if int(string) % 2023 == 0:
                print(string)


Task24_1()

# Task24_2()

# Task25_1()