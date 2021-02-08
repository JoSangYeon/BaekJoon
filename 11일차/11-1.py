"""
백준 알고리즘 14584번: 암호 해독
https://www.acmicpc.net/problem/14584
"""
import sys

def calc(key, n, words):
    for i in range(26):
        temp = ""
        for k in key:
            #1~26까지 카이사르 복호화한 것을 탐색해봄
            temp += chr(((ord(k)-97+i)%26)+97)

        for k in range(n):
            if words[k] in temp: # 해당 문자열이 temp에 포함되어있는지 확인
                return temp

def main():
    key = sys.stdin.readline()[:-1]
    n = int(sys.stdin.readline())
    words = []
    for i in range(n):
        word = input()
        words.append(word)

    print(calc(key, n, words))

if __name__ == "__main__":
    main()