"""
백준 알고리즘 1252번: 이진수 덧셈
https://www.acmicpc.net/problem/1252
"""
import sys

def main():
    n,m = sys.stdin.readline().split()
    n = int(n,2); m = int(m,2)

    result = n+m

    print(bin(result)[2:])

if __name__ == "__main__":
    main()