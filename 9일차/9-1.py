"""
백준 알고리즘 2914번: 저작권
https://www.acmicpc.net/problem/2914

평균 = 멜로디 / 수록곡
멜로디 = 수록곡 * 평균
멜로디를 수록곡으로 나눌때 수록곡의
갯수만큼의 오차 범위가 생긴다
따라서 수록곡*평균에 수록곡의 갯수를 빼주고 +1을 해주면 최소한의
멜로디 개수를 구할 수 있다.
"""
import sys

def calc(a, i):
    return (a*i)-a+1

def main():
    a, i = sys.stdin.readline().split()
    a = int(a); i = int(i)
    print(calc(a,i))

if __name__ == "__main__":
    main()