def calc(word, arr):
    words = {}
    for i in word:
        if i in words.keys():
            words[i] += 1
        else:
            words[i] = 1

    cnt = 0
    for w in arr:
        checkBool = True
        if len(word) != len(w):
            continue
        else:
            check = {}
            for ch in w:
                if ch not in words.keys():
                    checkBool = False
                    break
                else:
                    if ch in check.keys():
                        check[ch] += 1
                    else:
                        check[ch] = 1
            keys = words.keys()
            if len(words) != len(check):
                continue
            else:
                for i in keys:
                    if words[i] != check[i]:
                        checkBool = False
                        break
                if checkBool:
                    cnt += 1
    return cnt


def solution(word, arr):
    answer = calc(word, arr)
    return answer


if __name__ == "__main__":
    print(solution("cat", ["cat","dog","fish"]))