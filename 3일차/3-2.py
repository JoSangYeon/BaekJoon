import sys

c = int(input())
li = []
ns = []

for i in range(c):
    data = sys.stdin.readline().split()
    ns.append(int(data[0]))
    data = data[1:]
    data = [int(x) for x in data]
    li.append(data)

def calc(n, data):
    count = 0
    mean = float(sum(data) / n)

    for k in data:
        if k > mean:
            count += 1

    return float(count / n * 100.0)

for j in range(c):
    result = calc(ns[j], li[j])
    print("%.3f%%" %result)