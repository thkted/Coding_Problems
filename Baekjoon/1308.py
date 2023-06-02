# input
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
month = {1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

# function
def checkLeapYear(y):
    if y % 4 != 0:
        return False
    if y % 100 != 0:
        return True
    if y % 400 == 0:
        return True
    return False

def calculateDay(y, m, d):
    day = 0
    # year
    for i in range(y):
        if checkLeapYear(i):
            day += 1
        day += 365
    # month
    for i in range(1, m + 1):
        if i == 2:
            if checkLeapYear(y):
                day += 1
        day += month[i]
    # day
    day += d

    return day


# main
s_day = calculateDay(y1, m1, d1)
e_day = calculateDay(y2, m2, d2)
diff = e_day - s_day

if diff < 365243:
    print("D-{}".format(diff))
else:
    print("gg")
