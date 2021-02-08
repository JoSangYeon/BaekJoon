"""
백준 알고리즘 2839번: 설탕배달 
https://www.acmicpc.net/problem/2839
"""
import sys

def calc(n):
    # 정확하게 설탕을 담을 수 없는 경우는
    # -1로 예외처리 함
    if(n<3 or n == 4 or n == 7):
        return -1

    # 우선 5로 나눠서 5kg 봉지의 개수를 셈
    cnt5 = int(n/5)
    n = n%5 # 나머지 계산도 해줌

    # 이제 3으로 나눠서 3kg 봉지의 개수를 셈
    cnt3 = int(n/3)
    rema3 = n%3 # 그 나머지도 계산 해줌

    # 5로 나누고 3으로 나눴을때 나머지가
    # 0,1,2가 있는데 각자에 대한 처리
    if(rema3 == 0):
        # 나머지가 0일 경우 정확하게 떨어진 경우이므로 그냥 반환
        return cnt5+cnt3
    elif(rema3 == 1):
        # 나머지가 1인 경우 5kg보지를 하나 풀어서 1+5를 3kg봉지 2개로 만듦
        return (cnt5-1) + (cnt3+2)
    elif(rema3 == 2):
        # 나머지가 2인 경우 5kg 봉지를 2개 풀어서 2+10를 3kg봉지 4개로 만듦
        return (cnt5-2) + (cnt3+4)

def main():
    n = sys.stdin.readline()
    n = int(n)
    print(calc(n))

if __name__ == "__main__":
    main()