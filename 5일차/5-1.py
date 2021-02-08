"""
백준 알고리즘 10174번: 팰린드롬
https://www.acmicpc.net/problem/10174
"""
import sys

def calc():
    # txt1에 단어를 입력
    txt1 = list(sys.stdin.readline()[:-1])

    # txt1의 요소들 중에서 문자(isalpha)인 것을 모두 대문자(upper)로 변경
    for i in range(len(txt1)):
        if txt1[i].isalpha() == True:
            txt1[i] = txt1[i].upper()

    # txt1의 역순으로 저장된 txt2를 생성
    txt2 = list(txt1)
    txt2.reverse()

    # txt1과 txt2를 순차적으로 비교하고
    # 서로 다른 요소일때 바로 "No"를 리턴
    result = "No"
    for i in range(len(txt1)):
        if(txt1[i] == txt2[i]):
            result = "Yes"
        else:
            result = "No"
            break;
    return result

def main():
    n = sys.stdin.readline()
    n = int(n)
    for i in range(n): print(calc())

if __name__ == '__main__':
    main()