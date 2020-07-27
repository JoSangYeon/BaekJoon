# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
n = sys.stdin.readline()
n = int(n)

li = []
for i in range(n):
	b = []
	a = sys.stdin.readline().split(".")
	for j in a:
		b.append(int(j))
	li.append(b)

li.sort()

for i in range(n):
	line = ""
	for j in li[i]:
		line += str(j)+"."
	line = line[:-1]
	print(line)
	