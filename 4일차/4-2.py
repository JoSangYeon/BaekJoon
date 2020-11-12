"""
백준 알고리즘 17608번: 막대기
https://www.acmicpc.net/problem/17608
"""
import sys

def calc(height):
    # 가장 오른쪽에서 부터 시작함으로 가장 높은 탑의 높이를 저장
    max = height[-1]
    cnt = 1 #가장 오른쪽 타워는 보임으로 1부터 카운트

    # 0번 막대기 부터 마지막 막대기를 제외한 막대기 까지 역순으로 참조
    for i in range(len(height)-1,-1 , -1):
        # 참조한 막대기의 높이가 가장 높은 막대기 보다 높이가 크면 카운트
        if height[i] > max:
            cnt += 1
            max = height[i]
    return cnt

def main():
    n = sys.stdin.readline()
    n = int(n)

    height = []
    for i in range(n):
        height.append(int(sys.stdin.readline()))
    print(calc(height))

if __name__ == '__main__':
    main()