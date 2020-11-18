"""
백준 알고리즘 1297번: TV 크기
https://www.acmicpc.net/problem/1297

피타고라스의 정리: c^2 = a^2 + b^2
비율 h,w에 대하여 a:b = w:h(내항의 곱은 외항의 곱이 같음을 적용)
a*h = b*w => a = (w*b)/h
a^2 = (w*b*/h)^2 = (w/h)^2 * b^2
c^2 = (w/h)^2 * b^2 + b^2
b^2 = c^2 / (1+ (w/h)^2)
b = (c^2 / (1+ (w/h)^2))^0.5
a = b*w/h
위 방법은 답은 근사하게 나오나 백준에서 원하는 답은 안나오나 봄

대각선의 비율을 구함
r = (c^2 / (w^2 + h^2))**0.5
a = h*r, b = w*r
"""
import sys

def calc(inch, h, w):
    r = (inch**2 / (w**2 + h**2))**0.5
    a = h*r
    b = w*r
    return int(a), int(b)


def main():
    inch, h, w = sys.stdin.readline().split()
    inch = int(inch); h = int(h); w = int(w)
    a, b = calc(inch, h, w)
    print(a, b)

if __name__ == "__main__":
    main()