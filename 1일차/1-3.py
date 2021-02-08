import sys
n = sys.stdin.readline()
n = int(n)

def calc(n):
    if n%2==0:
        row = int(n / 2)
        col = int(n / 2)
    else:
        row = int(n/2)+1
        col = int(n/2)

    return (row+1) * (col+1)


print(calc(n))