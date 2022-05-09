# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
play = sys.stdin.readline()

play = int(play)

game_dic = {}
for i in range(play):
	n, m = sys.stdin.readline().split()
	n = int(n)
	m = int(m)
	if m not in game_dic.keys():
		game_dic[m] = 1
	else:
		game_dic[m] += 1

val = game_dic.values()

if max(list(game_dic.values())) > 2:
	print(0)
else:
	print(1)