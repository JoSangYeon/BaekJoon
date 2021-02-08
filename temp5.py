def make_segyun(n):
    days = [0, 1]

    for i in range(2, n + 1):
        temp = i // 2
        if i%2 == 0:
            days.append(days[temp])
        else:
            days.append(days[temp]+1)

    return days[-1]

print(make_segyun(50))