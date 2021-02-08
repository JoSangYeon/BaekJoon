"""
백준 알고리즘 2417번: 정수 제곱근
https://www.acmicpc.net/problem/2417
"""
import sys

def calc(n):
    # 딱 떨어지는 제곱근이 아닐 경우
    # ex) 17, 24, 33 등등
    if n**(0.5)%1 != 0:
        return int(n**(0.5))+1

    # 딱 떨어지는 제곱근일 경우
    # ex) 16, 25, 36 등등
    else: return int(n**(0.5))

def main():
    n = int(sys.stdin.readline())
    print(calc(n))

if __name__ == "__main__":
    main()