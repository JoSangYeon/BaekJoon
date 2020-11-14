"""
백준 알고리즘 2438번: 별찍기-1
https://www.acmicpc.net/problem/2438
"""
import sys

def calc(n):
    for i in range(1,n+1):
        for k in range(i):
            print("*",end='')
        print()

def main():
    n = sys.stdin.readline()
    n = int(n)
    calc(n)

if __name__ == "__main__":
    main()