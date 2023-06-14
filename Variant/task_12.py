def Task_12():
    for one in range(50):
        for two in range(50):
            for three in range(50):
                s = "0"+ "1" * one + "2" * two + "3" * three + "0"
                s_original = s
                while "00" not in s:
                    s = s.replace("01", "210", 1)
                    s = s.replace("02",  "3101", 1)
                    s = s.replace("03", "2012", 1)
                if s.count("1") == 61 and s.count("2") == 50 and s.count("3") == 18:
                    print(len(s_original))
                    quit()
Task_12()