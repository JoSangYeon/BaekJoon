"""
백준 알고리즘 8958번: OX 퀴즈
https://www.acmicpc.net/problem/8958
"""

def calc(n):
    result = [] # 점수를 담은 리스트 선언

    for i in range(n):
        answer = input() # OX를 입력 받음
        combo = 0        # 연속으로 맞힐 수록 +1
        sum = 0          # 최종적인 점수를 저장 할 변수
        for cho in answer:
            # X일 경우는 combo를 0로 초기화
            if cho == 'X':
                combo = 0
            # O일 경우 combo를 1만큼 늘리고 점수에 더해줌
            elif cho == 'O':
                combo += 1
                sum += combo
        result.append(sum) #연산을 마치면 리스트에 담음
    return result

def main():
    n = int(input())
    result = calc(n)
    for r in result: print(r)

if __name__=="__main__":
    main()