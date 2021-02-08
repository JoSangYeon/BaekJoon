"""
백준 알고리즘 1236번: 성 지키기
https://www.acmicpc.net/problem/1236
"""
import sys

def calc(n,m,castle):
    row_cnt = 0
    col_cnt = 0

    # 행을 기준으로 탐색
    for i in range(n):
        check = True
        for k in range(m):
            if castle[i][k] == 'X': #경비원이 있는 행이라면 스탑
                check = False
                break
        if check: row_cnt += 1

    # 열을 기준으로 탐색
    for i in range(m):
        check = True
        for k in range(n):
            if castle[k][i] == 'X': #경비원이 있는 열이라면 스탑
                check = False
                break
        if check: col_cnt += 1

    # 체크한 행과 열의 필요한 경비원의 수 중 큰 값을 반환
    return max(row_cnt, col_cnt)


def main():
    # 입력값을 받는 부분
    n,m = sys.stdin.readline().split()
    n = int(n); m = int(m)
    castle = []
    for i in range(n):
        castle.append(list(sys.stdin.readline()[:-1]))

    print(calc(n,m,castle))

if __name__ == "__main__":
    main()