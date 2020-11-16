"""
백준 알고리즘 11728번: 배열 합치기
https://www.acmicpc.net/problem/11728
"""
import sys

def calc(n,m,A,B):
    C = A+B # 단순하게 리스트를 합침
    C.sort() # 정렬
    return C

def main():
    n, m = sys.stdin.readline().split()
    n = int(n); m = int(m)

    A = sys.stdin.readline()[:-1].split()
    B = sys.stdin.readline()[:-1].split()
    A = [int(i) for i in A]
    B = [int(i) for i in B]

    result = calc(n,m,A,B)
    for i in result:
        print(i, end=" ")

if __name__ == "__main__":
    main()