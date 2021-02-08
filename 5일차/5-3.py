"""
백준 알고리즘 1920번: 수 찾기
https://www.acmicpc.net/problem/1920

해당 문제는 dictionary로 해결할 수 있음
A의 요소를 dictionary로 하고
m 만큼의 정수들(Barr라고 변수 설정함)을 해당 딕셔너리에서 존재 여부를 확인함
"""
import sys

def calc(n):
    # A에 대한 값을 입력 받음 공백 단위로 split
    Aarr = sys.stdin.readline()[:-1].split(' ')

    # m과 m만큼의 개수만큼의 정수를 입력 받음 Barr도 공백단위로 split
    m = int(sys.stdin.readline())
    Barr = sys.stdin.readline()[:-1].split(' ')

    # A에 대한 정보를 딕셔너리로 저장함
    Adict = {}
    for i in range(n):
        Adict[Aarr[i]] = True

    # Barr의 원소가 Adict의 key값에 있고, 그 key값의 value가 True일 경우 1을 삽입
    # 아닐 경우 0을 삽입
    result = []
    for i in range(m):
        if Barr[i] in Adict.keys() and Adict[Barr[i]] == True:
            result.append(1)
        else:
            result.append(0)

    return result

def main():
    n = int(sys.stdin.readline())
    result = calc(n)
    for i in result: print(i)

if __name__ == "__main__":
    main()