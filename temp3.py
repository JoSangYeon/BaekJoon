str1 = "Khoor Zruog!"
n = 3

li = list(str1)

print(li)

for i in range(len(li)):
    ch = ord(li[i])
    if 65 <= ch and ch <= 90:
        li[i] = ch
    elif 97 <= ch and ch <= 122:
        li[i] = ch
    else:
        continue

print(li)

for ch in li:
    if str(ch).isdigit():
        if 65 <= ch and ch <= 90:
            ch -= n
            if ch < 65:
                ch = 90 - (64 - ch)
        elif 97 <= ch and ch <= 122:
            ch -= n
            if ch < 97:
                ch = 122 - (96 - ch)
    else:
        continue

print(li)

for i in range(len(li)):
    if str(li[i]).isdigit():
        li[i] = chr(li[i])

print(li)

print("".join(li))

