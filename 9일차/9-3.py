"""
백준 알고리즘 1912번: 연속합
https://www.acmicpc.net/problem/1912

DP로 푸는 문제
점화식은 max(sum[i]+data[i], data[i+1])
해당 식의 의미는
지금까지 더해온 값 sum, 주어진 리스트 data에서
현재까지 더해온 값 sum[i]에서 data[i+1](다음 숫자)를 더한게 큰지
아니면 그냥 data[i+1](연속해서 더해 오던 것을 초기화 하는 것)한게
큰지 비교해서 더 큰 수를 추가하는 것
"""
import sys

def calc(n, data):
    sum = [data[0]]
    for i in range(len(data)-1):
        # 다음(i+1) 숫자와의 합이 큰지, 그냥 다시 연속해서 합을 구하는게 큰지 비교해서
        # sum 리스트에 추가함
        sum.append(max(sum[i]+data[i+1], data[i+1]))
    return max(sum)

def main():
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().split()
    data = [int(i) for i in data]
    print(calc(n,data))

if __name__ == "__main__":
    main()