import sys
a,b,n = sys.stdin.readline().split()
a = int(a)
b = int(b)
n = int(n)

def calc(a,b,n):
    li = []
    quot = 0
    rema = 0
    i = 0
    while(i != n+1):
        if(a<b & i == 0):
            a *= 10
            li.append(0);

        quot = int(a / b)
        rema = int(a % b)

        li.append(quot)

        a = rema*10

        i += 1

    return li


result = calc(a,b,n)
print(result[-1])