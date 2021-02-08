"""
백준 알고리즘 2747번: 피보나치 수
https://www.acmicpc.net/problem/2747

재귀함수로 안하고 동적프로그래밍 비스무리 하게 풀어봄
"""
import sys

fibo = [0, 1]

def calc(n):
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[n]


def main():
    n = int(sys.stdin.readline())
    print(calc(n))

if __name__ == "__main__":
    main()