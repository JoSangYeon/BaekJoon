import sys
n = sys.stdin.readline()
n = int(n)

def calc(n):
    if(n<3 or n == 4 or n == 7):
        return -1
    cnt5 = 0
    cnt3 = 0
    rema3 = 0

    cnt5 = int(n/5)
    n = n%5

    cnt3 = int(n/3)
    rema3 = n%3

    if(rema3 == 0):
        return cnt5+cnt3
    elif(rema3 == 1):
        return (cnt5-1) + (cnt3+2)
    elif(rema3 == 2):
        return (cnt5-2) + (cnt3+4)


print(calc(n))

print(True || False)