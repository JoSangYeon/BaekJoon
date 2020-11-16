"""
백준 알고리즘 1436번: 영화감독 숌
https://www.acmicpc.net/problem/1436

https://namu.wiki/w/%EB%B8%8C%EB%A3%A8%ED%8A%B8%20%ED%8F%AC%EC%8A%A4
브루트 포스(Brute Force) 기법 사용하여 무식하게 탐색하는 방법
원시적으로 대입 노가다 뛰어서 답을 구함
"""
import sys

def calc(n):
    num = 666 # n = 1일때부터 카운트 시작

    while n != 0: # n이 0이 될때까지 반복
        if "666" in str(num): # 해당 숫자(num)가 666을 포함하면 n -= 1을 수행 
            n -= 1
        num += 1 # 계속해서 num += 1로 값을 갱신
    return num-1

def main():
    n = int(sys.stdin.readline())
    print(calc(n))

if __name__ == "__main__":
    main()