"""
백준 알고리즘 7568번: 덩치
https://www.acmicpc.net/problem/7568
"""
import sys

def calc(n, data):
    result = [1 for _ in range(n)] #결과를 저장할 순위 list
    for i in range(n): #2중 for문
        for k in range(n):
            #한명의 사람에 대해 모든 사람의 덩치를 탐색
            if data[i][0] > data[k][0] and data[i][1] > data[k][1]:
                result[k] += 1 #조건에 해당되면 순위를 +1함

    return " ".join([str(ch) for ch in result]) #출력

def main():
    # n과 사람들의 덩치 데이터를 받아오는 부분
    n = int(input())
    data = []
    for i in range(n):
        x,y = sys.stdin.readline().split()
        x = int(x); y = int(y)
        data.append((x,y))

    print(calc(n, data))


if __name__ == "__main__":
    main()