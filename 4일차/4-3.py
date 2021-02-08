"""
백준 알고리즘 1037번: 약수
https://www.acmicpc.net/problem/1037
"""
import sys

def calc(n, realYakSu):
    realYakSu.sort() # 오름 차순으로 정렬 시킨다.
    return realYakSu[0] * realYakSu[n-1]


def main():
    n = sys.stdin.readline()
    n = int(n)

    realYakSu = sys.stdin.readline().split()
    realYakSu = [int(yaksu) for yaksu in realYakSu]

    print(calc(n, realYakSu))

if __name__ == "__main__":
    main()