"""
백준 알고리즘 1059번: 좋은 구간
https://www.acmicpc.net/problem/1059
"""
import sys

def calc(L, s, n):
    if n in s:
        return 0

    a = 0
    b = 0
    for i in s:
        if n>i:
            a = i+1
        else:
            b = i-1
            break;

    return b-a+((b-n)*(n-a))

def main():
    L = int(sys.stdin.readline())
    s = (sys.stdin.readline()[:-1]).split(" ")
    s = [int(_) for _ in s]; s.insert(0,0); s.sort()
    n = int(sys.stdin.readline())

    print(calc(L, s, n))

if __name__ == "__main__":
    main()