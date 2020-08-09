# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

def calc(a,b,c,n,li):
	num = 0; cost = 0
	
	for i in range(n):
		if li[i][1] == 0:
			if a != 0:
				a -= 1
				num += 1
				cost += li[i][0]
			elif c != 0:
				c -= 1
				num += 1
				cost += li[i][0]
		else:
			if b != 0:
				b -= 1
				num += 1
				cost += li[i][0]
			elif c != 0:
				c -= 1
				num += 1
				cost += li[i][0]
	return num, cost

a, b, c = sys.stdin.readline().split(" ");
a = int(a); b = int(b); c = int(c)

n = int(sys.stdin.readline())

li = []
for i in range(n):
	app = []
	ci, ti = sys.stdin.readline().split(" ");
	ci = int(ci); ti = int(ti)
	app.append(ci); app.append(ti)
	li.append(app)
	
li.sort()

num, cost = calc(a,b,c,n,li)
print(num, cost)