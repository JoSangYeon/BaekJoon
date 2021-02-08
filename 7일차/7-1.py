"""
백준 알고리즘 2693번: N번째 큰 수
https://www.acmicpc.net/problem/2693

파이썬으로 풀경우 정렬 한 후에 인덱스 접근할때 음수로 접근하면 된다.
"""
import sys

def calc(data):
    data.sort() # 정렬
    return data[-3] #인덱스 접근을 역순으로 한다(==뒤에서 3번째)

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        data = sys.stdin.readline()[:-1].split()
        data = [int(i) for i in data]
        print(calc(data))

if __name__ == "__main__":
    main()