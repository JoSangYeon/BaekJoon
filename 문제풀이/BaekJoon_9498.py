"""
백준 알고리즘 9498번: 시험 성적
https://www.acmicpc.net/problem/9498
"""
import sys

def calc(n):
    if n >= 90:
        return "A"
    elif n>=80 and n<=89:
        return "B"
    elif n>=70 and n<=79:
        return "C"
    elif n>=60 and n<=69:
        return "D"
    else:
        return "F"

def main():
    n = int(sys.stdin.readline())
    print(calc(n))

if __name__ == "__main__":
    main()