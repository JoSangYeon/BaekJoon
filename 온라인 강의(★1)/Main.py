# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
h1, m1 = sys.stdin.readline().split(":")
h2, m2 = sys.stdin.readline().split(":")

h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)

time1 = h1*60 + m1
time2 = h2*60 + m2

if time2 <= time1+10 and time1 <= time2:
	print(1)
else:
	print(0)