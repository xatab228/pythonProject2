
def task12():
    start = '1' * 81
    while (start.find('1111') > -1) or (start.find('88888') > -1):
        if start.find('1111') > -1:
            start = start.replace('1111','888',1)
        else:
            start = start.replace('88888', '888', 1)
    return start

print(task12())