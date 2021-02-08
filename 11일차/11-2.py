"""
백준 알고리즘 1920번: 수 찾기
https://www.acmicpc.net/problem/1920
"""
import sys

def calc(n):
    Aarr = sys.stdin.readline()[:-1].split(' ')
    Aarr = set([int(_) for _ in Aarr])
    m = int(sys.stdin.readline())
    Barr = sys.stdin.readline()[:-1].split(' ')

    result = []
    for i in range(m):
        if int(Barr[i]) in Aarr:
            result.append(1)
        else:
            result.append(0)

    return result

def main():
    n = int(sys.stdin.readline())
    result = calc(n)
    for i in result: print(i)

if __name__ == "__main__":
    main()