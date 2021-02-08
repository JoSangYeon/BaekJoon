"""
백준 알고리즘 1049번: 기타줄
https://www.acmicpc.net/problem/1049
"""
import sys

def calc(n,m):
    info = [[],[]]
    for i in range(m):
        pak, one = sys.stdin.readline().split()
        info[0].append(int(pak))
        info[1].append(int(one))

    # 여섯개 세트와 낱개 가격들 중 가장 저렴한 것을 선택
    pakage = min(info[0])
    single = min(info[1])

    price = 0 # 지불해야하는 금액
    while n>0: # 기타줄 = n이 0이 될때까지
        if n>=6: # n이 6이상일때
            # 세트가격이 낱개 6개보다 비싸면
            if pakage > single*6:
                price += single*n #낱개로 모든 기타줄 구매
                n -= n
            #낱개 6개가 세트보다 비싸면
            else:
                price += pakage #세트를 구입
                n -= 6
        else: # 기타줄이 6미만일때
            # 남은 기타줄 만큼의 낱개 가격과 세트 가격을 비교
            if pakage < single*n:
                price += pakage
                n -= 6
            else:
                price += single*n
                n -= n

    return price

def main():
    n, m = sys.stdin.readline().split()
    n=int(n); m=int(m)

    print(calc(n, m))

if __name__ == "__main__":
    main()