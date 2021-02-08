"""
백준 알고리즘 1157번: 단어 공부
https://www.acmicpc.net/problem/1157
"""
import sys

def calc(n):
    dic = {}

    # 각각의 문자에 대해 탐색
    for str in n:
        if(str.upper() in dic): # 대소문자 구분을 없앰
            dic[str.upper()] += 1
        else:
            dic[str.upper()] = 1

    max = 0
    flag = 0
    keyword = ""
    for key in dic.keys(): # 가장 많은 알파벳을 탐색
        if dic[key] > max:
            max = dic[key]
            keyword = key

    for key in dic.keys(): # 가장 많은 알파벳이 여러개일 경우 처리
        if dic[key] == max:
            flag += 1

    return flag, keyword


def main():
    n = sys.stdin.readline()
    n = n[:-1]
    flag, keyword = calc(n)
    if (flag > 1):
        print("?")
    else:
        print(keyword)

if __name__ == "__main__":
    main()