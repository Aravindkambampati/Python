def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
        return leap
    elif year % 100 != 0:
        if year % 4 == 0:
            leap = True
            return leap
        else:
            return leap
    else:
        return leap
print(is_leap(1800))