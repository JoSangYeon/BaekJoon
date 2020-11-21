"""
백준 알고리즘 2446번: 별찍기-9
https://www.acmicpc.net/problem/2446
"""
import sys

def calc(n):
    for i in range(n,1,-1):
        for k in range(n-i):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end="")
        print()
    for i in range(1,n+1):
        for k in range(n-i):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end="")
        print()

def main():
    n = int(sys.stdin.readline())
    calc(n)

if __name__ == "__main__":
    main()