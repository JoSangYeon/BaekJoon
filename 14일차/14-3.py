"""
백준 알고리즘 1259번: 팰린드롬 수
https://www.acmicpc.net/problem/1259
"""
import sys

def calc(num_list):
    for num in num_list:
        check = 'yes'
        n = len(num)-1 #마지막 인덱스를 참조하는 변수
        for i in range(len(num)//2):
            if num[i] != num[n-i]:
                check = 'no'
                break
        print(check)

def main():
    num = ""
    num_list = []
    while num != '0':
        num = sys.stdin.readline()[:-1]
        num_list.append(num)
    num_list = num_list[:-1]

    calc(num_list)


if __name__ == "__main__":
    main()