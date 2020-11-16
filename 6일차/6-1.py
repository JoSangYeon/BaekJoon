"""
백준 알고리즘 1924번: 2007년
https://www.acmicpc.net/problem/1924

월/일로 되어있는 자료를 일로 바꿔주고 나눠서 나머지가
0~6이면 각각 일~토 이므로 알맞게 매칭해서 해결한다.
"""
import sys
# 날짜별로 arr 선언
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
# 각 달마다 일의 누적 합 arr 선언
month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

def calc(x, y):
    dayCnt = month[x-1] + y # 전체 일수를 확인
    return day[dayCnt % 7] # 나머지를 인덱스로 넣어서 날짜를 리턴

def main():
    x, y = sys.stdin.readline().split()
    x = int(x); y = int(y)
    print(calc(x, y))

if __name__ == "__main__":
    main()