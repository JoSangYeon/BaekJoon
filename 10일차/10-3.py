"""
백준 알고리즘 2446번: 별찍기-10
https://www.acmicpc.net/problem/2447

프랙탈 도형 만들기
분할 정복 알고리즘으로 문제를 해결 할 수 있다.
https://j3sung.tistory.com/65
"""
import sys

n = int(sys.stdin.readline())
star = [[" " for i in range(n)] for i in range(n)]

def show():
    for i in range(len(star)):
        for k in range(len(star[i])):
            print(star[i][k],end="")
        print()

def calc(n, x, y):
    if n == 1:
        star[y][x] = "*"
        return
    else:
        temp = n//3
        for i in range(3):
            for k in range(3):
                if i!=1 or k!=1:
                    calc(temp, x + (temp * i), y + (temp * k))

def main():
    calc(n,0,0)
    show()

if __name__ == "__main__":
    main()