"""
백준 알고리즘 14681번: 사분면 고르기
https://www.acmicpc.net/problem/14681
"""
import sys

def calc(x,y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

def main():
    x = int(sys.stdin.readline())
    y = int(sys.stdin.readline())
    print(calc(x,y))

if __name__ == "__main__":
    main()