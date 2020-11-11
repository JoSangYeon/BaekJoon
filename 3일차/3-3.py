def calc():
    selfNum = [True for i in range(10001)]

    for i in range(1,10001):
        temp = i
        for x in range(len(str(i))):
            temp += int(str(i)[x])
        if (temp > 10000):
            continue
        else:
            selfNum[temp] = False

    for i in range(1, 10000):
        if(selfNum[i] == True):
            print(i)

calc()