"""
백준 알고리즘 2739번: 구구단
https://www.acmicpc.net/problem/2739
"""
import sys

def calc(n):
    for i in range(1, 10):
        print("%d * %d = %d" %(n,i,(n*i)))
        # print(n, "*", i, "=", (n*i)

def main():
    n = int(sys.stdin.readline())
    calc(n)

if __name__ == "__main__":
    main()