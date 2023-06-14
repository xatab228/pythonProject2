def Task_24():
    file = open('files/24.txt')
    counter = 0
    string = file.readline()
    line = string.split('PP')
    for letter in string:
        if letter != 'P':
            counter += 1
        else:
