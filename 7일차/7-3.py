"""
백준 알고리즘 1769번: 3의 배수
https://www.acmicpc.net/problem/1769
"""
import sys

def calc(n):
    cnt = 0 # 변환한 개수를 count

    # n의 길이가 1이 될때까지 반복
    while len(n) != 1:
        n = [int(i) for i in n] # n의 요소들을 int로 변경
        n = sum(n) # n의 요소들의 합을 구함
        n = list(str(n)) # n의 요소들을 한글자 단위로 split()
        cnt += 1 # count 갱신

    # 3으로 나눠떨어지면 YES
    if(int(n[0]) % 3 == 0):
        return str(cnt)+"\nYES"
    else: # 그 외는 NO
        return str(cnt)+"\nNO"

def main():
    n = list(sys.stdin.readline()[:-1])
    print(calc(n))

if __name__ == "__main__":
    main()