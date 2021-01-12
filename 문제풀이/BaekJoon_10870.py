"""
백준 알고리즘 10870번: 피보나치 수 5
https://www.acmicpc.net/problem/10870
"""
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input())
    print(fibonacci(n))

if __name__ == "__main__":
    main()