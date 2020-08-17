# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
n,m = sys.stdin.readline().replace("\n","").split()

n = int(n)
m = int(m)

num = sys.stdin.readline().replace("\n","").split()
li = list(map(lambda x: int(x), num))

lili = []
for i in range(len(li)):
	if(i==0):
		lili.append(li[i])
	else:
		lili.append(lili[i-1]+li[i])
		
ma = -1
for i in range(n):
	temp = (lili[i] % m) + ((lili[-1] - lili[i]) % m);
	if(ma < temp):
		ma = temp
		
print(ma)