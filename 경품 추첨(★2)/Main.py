import sys
n,m = sys.stdin.readline().split()
n = int(n)
m = int(m)
ans = [0 for i in range(m)]
stu_input = sys.stdin.readline().split()
sch_input = sys.stdin.readline().split()

stu_dict = {}
for i in range(n):
    if stu_input[i] not in stu_dict.keys():
        stu_dict[stu_input[i]] = 1
    else:
        stu_dict[stu_input[i]] += 1

for i in range(m):
    if sch_input[i] not in stu_dict.keys():
        print("0 ",end="")
    else:
        print(str(stu_dict[sch_input[i]]) + " ",end="")