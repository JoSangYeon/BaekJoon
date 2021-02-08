"""
백준 알고리즘 10818번: 최소, 최대
https://www.acmicpc.net/problem/10818
"""
import sys

def calc(n, data):
    return str(min(data)) + " " + str(max(data))


def main():
    n = int(sys.stdin.readline())
    data = sys.stdin.readline()[:-1].split()
    data = [int(_) for _ in data]
    print(calc(n, data))

if __name__ == "__main__":
    main()