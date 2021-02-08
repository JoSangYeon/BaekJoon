"""
백준 알고리즘 2004번: 조합 0의 개수
https://www.acmicpc.net/problem/2004

nCr = n!/((n-r)! * r!)
아 시간초과...
0의 개수는 10이 생겨날때마다 늘어난다.
10 = 2 * 5로만들어짐 따라서
분자 n의 5의 개수에서 m, n-m의 5의 개수를 빼고(약분 하는 거임)
분자 n의 2의 개수에서 m, n-m의 2의 개수를 뺀다(약분)
2는 100개 있는데 5가 1개있으면 10은 1개 만들어 지므로
둘중에 제일 작은 수를 구하면 그게 답 
"""
import sys

def count2(n):
    count = 0
    while n != 0:
        n = n//2
        count += n
    return count

def count5(n):
    count = 0
    while n != 0:
        n = n//5
        count += n
    return count

def calc(n, m):
    cnt2 = count2(n) - (count2(m) + count2(n - m))
    cnt5 = count5(n) - (count5(m) + count5(n-m))
    return min(cnt2, cnt5)

def main():
    n, m = sys.stdin.readline().split()
    n = int(n); m = int(m)
    print(calc(n,m))

if __name__ == "__main__":
    main()