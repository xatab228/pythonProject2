def Task_23(start, end):
    if start == end: return 1
    if start > end or start == 12: return 0
    if start < end:
        return (Task_23(start + 1, end) + Task_23(start + 2, end) + Task_23(start * 3, end))
result = Task_23(2, 9) * Task_23(9, 19)
print(result)