import sys
n = sys.stdin.readline()
n = n[:-1]

def calc(n):
    dic = {}

    for str in n:
        if(str.upper() in dic):
            dic[str.upper()] += 1
        else:
            dic[str.upper()] = 1

    max = 0
    flag = 0
    keyword = ""
    for key in dic.keys():
        if(dic[key] > max):
            max = dic[key]
            keyword = key

    for key in dic.keys():
        if(dic[key] == max):
            flag += 1

    return flag, keyword



flag, keyword = calc(n)

if(flag > 1):
    print("?")
else:
    print(keyword)