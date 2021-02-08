"""
백준 알고리즘 10828번: 스택
https://www.acmicpc.net/problem/10828
"""
import sys

class Stack:
    def __init__(self):
        self.s_list = []
        self.top = -1

    def is_empty(self):
        return int(self.top == -1)

    def push(self, x):
        self.top += 1
        self.s_list.insert(self.top, x)

    def pop(self):
        if self.is_empty():
            return -1
        else:
            temp = self.s_list[self.top]
            self.top -= 1
            return temp

    def get_size(self):
        return self.top+1

    def get_top(self):
        if self.is_empty():
            return -1
        return self.s_list[self.top]

def main():
    s = Stack()
    n = int(sys.stdin.readline())
    for i in range(n):
        cmd = input()
        if cmd[:2] == "pu":
            cmd = cmd.split()[-1]
            s.push(int(cmd))
        elif cmd == "top":
            print(s.get_top())
        elif cmd == "size":
            print(s.get_size())
        elif cmd == "pop":
            print(s.pop())
        elif cmd == "empty":
            print(s.is_empty())
        else:
            continue

if __name__ == "__main__":
    main()