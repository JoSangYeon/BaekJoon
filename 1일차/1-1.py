a = int(input())

def calc(origin, num, cycle):

    li = list(str(num))

    while(True):
        if (num == 0):
            return 1
        elif len(li) < 2:
            li.insert(0,"0")

        result = int(li[0]) + int(li[1])
        li2 = list(str(result))
        newNum = int(li[-1] + li2[-1])
        li = [li[-1], li2[-1]]

        if (newNum == origin):
            return cycle+1
        else:
            cycle += 1
            num = newNum

result = calc(a, a, 0)
print(result)