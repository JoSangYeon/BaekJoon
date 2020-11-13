"""
백준 알고리즘 7785번: 회사에 있는 사람
https://www.acmicpc.net/problem/7785

해당 문제는 dictionary로 풀면 된다.
이름 별로 enter인지 leave인지 각 key값에 매칭시켜주고
각 key에 대해 enter인 key만 리턴하면 됌

그리고 출력 결과를 정렬하여 출력해야되는거 같음
"""
import sys

def calc(n):
    # 출퇴근 로그를 입력 받음
    log = ""
    for i in range(n):
        log += sys.stdin.readline()

    # 출퇴근 로그를 가공하는 작업
    log = log.split('\n')[:-1] # 줄 단위로 분리
    log = [log[i].split(' ') for i in range(n)] # 이름과 (enter or leave)로 분리

    # 출퇴근 로그를 정리할 dictionary선언
    logDict = {}
    for i in range(n):
        logDict[log[i][0]] = log[i][1] # 이름(log[i][0])은 key로 상태(log[i][1])는 value로 저장

    # 리턴할 값을 구하는 과정
    result = []
    for i in logDict.keys():
        # 해당 직원의 상가 'enter'일 경우에만 result에 삽입
        if logDict[i] == 'enter':
            result.append(i)

    result = sorted(result, reverse=True) # 출력전에 정렬(무슨 정렬인진 모르겟음...? 내림 차순인가)
    return result

def main():
    n = int(sys.stdin.readline())
    result = calc(n)
    for i in range(len(result)): print(result[i])

if __name__ == "__main__":
    main()