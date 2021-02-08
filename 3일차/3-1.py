import sys
n = sys.stdin.readline()
n = n[:-1].split(" ")


def calc(n):
    count = 0
    for i in n:
        if(i == ''):
            continue
        count += 1

    return count


print(calc(n))

