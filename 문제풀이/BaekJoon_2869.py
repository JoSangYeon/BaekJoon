"""
백준 알고리즘 2869번: 달팽이는 올라가고 싶다.
https://www.acmicpc.net/problem/2869
"""
import sys, math

def calc(a,b,v):
    # a-b: 달팽이가 하루동안 이동한 길이
    # v-b: 도착한 날에 후진하는 b를 뺀 값
    day = (v-b) / (a-b)

    # 나눠떨어지지 않은 경우를 위한 소수점 올리 처리
    return math.ceil(day)


def main():
    a, b, v = sys.stdin.readline().split()
    a=int(a); b=int(b); v=int(v)
    print(calc(a,b,v))

if __name__ == "__main__":
    main()