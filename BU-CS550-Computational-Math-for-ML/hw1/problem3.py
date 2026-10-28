# Problem 3

def count_mondays():

    #leap year identify
    def is_leapyear(year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    #month identifier
    def days_inmonth(month, year):
        if month == 2:
            if is_leapyear(year):
                return 29
            else:
                return 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    # weekday identifier
    def weekday(day):
        if day == 0:
            return "Monday"
        elif day == 1:
            return "Tuesday"
        elif day == 2:
            return "Wednesday"
        elif day == 3:
            return "Thursday"
        elif day == 4:
            return "Friday"
        elif day == 5:
            return "Saturday"
        elif day == 6:
            return "Sunday"

    # moves calendar forward by 1 day
    def time_move(date, month, year, day):
        day = day + 1

        if day > 6:
            day = 0

        date = date + 1

        if date > days_inmonth(month, year):
            date = 1
            month = month + 1

            if month > 12:
                month = 1
                year = year + 1

        return date, month, year, day

    #starting point
    date = 1
    month = 1
    year = 1900
    day = 0

    count = 0

    while year < 2001:
        if year >= 1901:
            if date == 2:
                if day == 0:
                    count = count + 1

        date, month, year, day = time_move(date, month, year, day)

    return count


print(count_mondays())