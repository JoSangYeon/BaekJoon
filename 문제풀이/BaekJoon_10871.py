"""
백준 알고리즘 10871번: X보다 작은 수
https://www.acmicpc.net/problem/10871
"""
def main():
    ### n,x값을 받는다.###
    n, x = input().split()
    n = int(n);
    x = int(x)

    ### 비교할 숫자를 입력 받는다.###
    num_list = input().split(" ")
    num_list = [int(i) for i in num_list]
    """
    for i in range(len(num_list)):
       num_list[i] = int(num_list[i])
    """

    ### n개의 숫자를 비교한다.
    for i in range(n):
        if num_list[i] < x:
            print(num_list[i], end=" ")

if __name__ == "__main__":
    main()