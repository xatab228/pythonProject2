def task18430():
    # print("x y z w   F")
    print("w z y x   F")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                for w in range(0, 2):
                    if not ((x and y) or (y == z) or w):
                        # print(x, y, z, w, '| 0')
                        print(w, z, y, x, '| 0')


def task18550():
    print("x y z w   F")
    # print("z w y x   F")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                for w in range(0, 2):
                    if ((y <= z) or (not x and w)) == (w == z):
                        print(x, y, z, w, '| 1')
                        # print(z, w, y, x, '| 1')

print('Task 18430, answer: wzyx')
task18430()

# print('Task 18550, answer: zwyx')
# task18550()