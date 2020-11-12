"""
백준 알고리즘 1037번: 약수
https://www.acmicpc.net/problem/1037
"""
import sys

def calc(n, realYakSu):
    realYakSu.sort() # 오름 차순으로 정렬 시킨다.
    if n%2 == 0:
        # 약수의 개수가 짝수이면 가운데 2개의 약수의곱을 리턴
        # ex) 20= 2, 4*, 5*, 10
        return realYakSu[int(n/2)] * realYakSu[int(n/2) -1]
    else:
        # 약수의 개수가 홀수이면 가운데 1개의 약수의 제곱을 리턴
        # ex) 16= 2, 4*, 8
        return realYakSu[int(n/2)]**2


def main():
    n = sys.stdin.readline()
    n = int(n)

    realYakSu = sys.stdin.readline().split()
    realYakSu = [int(yaksu) for yaksu in realYakSu]

    print(calc(n, realYakSu))

if __name__ == "__main__":
    main()