"""
백준 알고리즘 1914번: 하노이 탑
https://www.acmicpc.net/problem/1914
"""
import sys

def hanoi(n, one, two, three):
    if n == 1:
        print(one, three)
    else:
        hanoi(n-1,one, three, two)
        print(one, three)
        hanoi(n-1, two, one, three)

def calc(n):
    cnt = (2 ** n) - 1
    print(cnt)
    if n <= 20:
        hanoi(n,1,2,3)

def main():
    calc(n)

if __name__ == "__main__":
    main()