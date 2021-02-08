def show(li):
    for i in range(len(li)):
        for j in range(len(li[i])):
            print(li[i][j], end=" ")
        print()


def fibo(n):
    fibo = [0, 1]

    for i in range(2, n * n + 1):
        fibo.append(fibo[i - 1] + fibo[i - 2])

    return fibo[1:]


def calc(f_list, n):
    li = [[0 for col in range(n)] for row in range(n)]

    idx = 0
    go = 1
    i =0; j = -1
    while True:
        for _ in range(n):
            j += go
            li[i][j] = f_list[idx]
            idx += 1
        n -= 1
        if n < 1:
            break;
        for _ in range(n):
            i += go
            li[i][j] = f_list[idx]
            idx += 1
        go = -go

    return li


n = int(input())

f_list = fibo(n)
li = calc(f_list, n)

show(li)