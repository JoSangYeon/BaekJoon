"""
백준 알고리즘 2941번: 크로아티아 알파벳
https://www.acmicpc.net/problem/2941
"""
import sys

# 크로아티아 알파벳 리스트
data = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

def calc(alpha):
    cnt = len(alpha) # 입력 문자열의 전체길이
    for ch in data:
        cnt -= alpha.count(ch) # 크로아티아 알파벳의 개수 만큼 뺀다.
    return cnt

def main():
    alpha = sys.stdin.readline()[:-1]
    print(calc(alpha))

if __name__ == "__main__":
    main()