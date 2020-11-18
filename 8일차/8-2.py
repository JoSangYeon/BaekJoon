"""
백준 알고리즘 2530번: 인공지능 시계
https://www.acmicpc.net/problem/2530

처음엔 3600, 60으로 나눠서 했는데 안되길래
너무 화나서 그냥 1씩 더해서 시간 계산하게 바꿈
일해라 컴퓨터!
"""
import sys

def calc(a,b,c,time):
    h = a; m = b; s = c
    while time>0:
        s += 1
        if s == 60:
            s = 0
            m += 1
            if m == 60:
                m = 0
                h += 1
                if h == 24:
                    h = 0
        time -= 1
    return h,m,s

def main():
    a, b, c = sys.stdin.readline().split()
    a= int(a); b= int(b); c= int(c)
    time = int(sys.stdin.readline())
    h,m,s = calc(a,b,c,time)
    print(h, m, s)

if __name__ == "__main__":
    main()