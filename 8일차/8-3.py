"""
백준 알고리즘 11053번: 가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/11053

증가하는 부분 수열: 동적프로그래밍(Dynamic programming)으로 풀 수 있는 기초적인 문제

참고
https://post.naver.com/viewer/postView.nhn?volumeNo=27105374&memberNo=33264526
https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4
"""
import sys

def calc(n, data):
    # 해당 변수는 data 배열에서 해당 각각의 인덱스까지 중 가장 긴 증가수열의 길이를 담는다.
    # 답을 구해 놓은걸 또 사용하기 위한 변수임
    lenArr = [1 for i in range(n)]
    for i in range(1,n):
        for k in range(i):
            if data[i] > data[k]: #현재 인덱스(i)의 값이 그 이전의 인덱스(k) 값보다 크면
                lenArr[i] = max(lenArr[i],lenArr[k]+1)
                # 인덱스 i까지의 data 배열의 증가하는 수열의 길이는 lenArr[i]와 이전 인덱스(k)에서
                # 가장 긴 증가수열의
                # 길이에서 +1(자기 자신을 추가하면 길이가 +1 되는 것)한 값을 비교하여
                # lenArr[i]에 저장함, 즉 lenArr는 이전까지의 길이를 담고 있는 것
                # 탐색 중에 증가하는 수를 찾았을 때(18 line), 해당 인덱스(k)에서 가장 긴 증가수열을 비교함
    return max(lenArr)



def main():
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().split()
    data = [int(i) for i in data]
    print(calc(n, data))

if __name__ == "__main__":
    main()