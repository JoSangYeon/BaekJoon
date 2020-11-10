import sys
a,b,c = sys.stdin.readline().split()
a = int(a)
b = int(b)
c = int(c)

def calc(a, b, c):
    if(b>=c):
        return -1

    return int(a/(c-b) + 1)

print(calc(a,b,c))