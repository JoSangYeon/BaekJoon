"""
백준 알고리즘 1206번: 사람의 수
https://www.acmicpc.net/problem/1206
"""
import sys

def main():
    n = int(sys.stdin.readline())

    numbers = []
    for _ in range(n):
        numbers.append(sys.stdin.readline()[:-1])
    numbers = list(int(float(i) * 1000 + 0.5) for i in numbers)

    ret = 1
    while True:
        candidate = [1000 * i // ret for i in range(10 * ret + 1)]
        if all([x in candidate for x in numbers]):
            print(ret)
            break
        ret += 1

if __name__ == '__main__':
    main()