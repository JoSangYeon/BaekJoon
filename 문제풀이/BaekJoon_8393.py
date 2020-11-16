"""
백준 알고리즘 8393번: 합
https://www.acmicpc.net/problem/8393
"""
import sys

def calc(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def main():
    n = int(sys.stdin.readline())
    print(calc(n))

if __name__ == "__main__":
    main()