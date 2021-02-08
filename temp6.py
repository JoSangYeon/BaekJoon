from hashlib import md5

def solution(string1, string2):

    str1 = md5(string1.encode()).hexdigest()
    str2 = md5(string2.encode()).hexdigest()

    answer = 32
    for i in range(32):
        if str1[i] == str2[i]:
            answer -= 1
    return answer

if __name__ == "__main__":
    print(solution('devil', 'angel'))
    print(solution('tree', 'tre'))