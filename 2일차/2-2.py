"""
백준 알고리즘 1157번: 단어 공부
https://www.acmicpc.net/problem/1157
"""
import sys

def calc(a,b,n):
    li = []
    i = 0
    while i != n+1:
        # a가 b보다 작을때
        if a < b:
            a *= 10
            li.append(0)

        # 몫과 나머지를 구해 a를 갱신한다.
        quot = int(a / b)
        rema = int(a % b)

        li.append(quot)
        a = rema*10
        i += 1
    return li[n]

def main():
    a, b, n = sys.stdin.readline().split()
    a = int(a); b = int(b); n = int(n)
    print(calc(a,b,n))

if __name__ == "__main__":
    main()