"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

# leap year occurs if year % 4 == 0 unless year is century

# 1  Jan = 31
# 2  Feb = 28, Feb = 29 on leap
# 3  Mar = 31
# 4  Apr = 30 !
# 5  May = 31
# 6  Jun = 30 !
# 7  Jul = 31
# 8  Aug = 31
# 9  Sep = 30 !
# 10 Oct = 31
# 11 Nov = 30 !
# 12 Dec = 31

# (1,jan,1901,) to (31,Dec
def gen_date(conds=[31,12,2000]):
    """generates all the dates up to the specified conditions
       conditions go in (day,month,year)"""
    # data format is (counter,day,date,month,year,BOOL <- for leap year)

    start = [[0,'Mon',1,1,1900,False]]
    temp = start[-1][2:-1]
    while temp != conds:
        start.append(update(start[-1]))
        temp = start[-1][2:-1]

    return start

def update(data):
    """updates the entered data"""
    data = data[:]
    data = update_counter(data)
    data = update_day(data)
    data = update_leap(data)
    data = update_date(data)
    
    return data

def update_date(data):
    """updates date,month,year"""
    modulus = calculate_mod(data)
    temp = (data[2] + 1) % modulus
    if temp == 0:
        data[2] = modulus
    else:
        data[2] = temp
    if data[2] == 1:
        data = update_month(data)
    return data

def update_month(data):
    """updates the month"""
    temp = (data[-3] + 1) % 12
    if temp == 0:
        data[-3] = 12
    else:
        data[-3] = temp
    if data[-3] == 1:
        data = update_year(data)
    return data

def update_year(data):
    """updates the year"""
    data[-2] = data[-2] + 1
    return data

def calculate_mod(data):
    """finds the number of days in a month"""
    months = { 1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7:31, 8: 31,
               9: 30, 10: 31, 11: 30, 12: 31}
    if data[-1] == True:
        months[2] = 29
    else:
        months[2] = 28
    return months[data[-3]]

def update_counter(data):
    data[0] = data[0] + 1
    return data

def update_day(data):
    """cycles through mon to sun"""
    days = [[1, 'Mon'],
            [2, 'Tue'], 
            [3, 'Wed'],
            [4, 'Thu'],
            [5, 'Fri'], 
            [6, 'Sat'],
            [7, 'Sun']]

    days1 = { x[1]: x[0] for x in days}
    days2 = { x[0]: x[1] for x in days}
    if ((days1[data[1]] + 1) % 7) == 0:
        data[1] = days2[7]
    else:
        data[1] = days2[(days1[data[1]] + 1) % 7]
    return data

def update_leap(data):
    """checks if leap year bool is supposed to be on, flips in on if needed"""
    if data[-2] % 400 == 0:
        data[-1] = True
    elif data[-2] % 100 == 0:
        data[-1] = False
    elif data[-2] % 4 == 0:
        data[-1] = True
    else:
        data[-1] = False
    return data

k = gen_date()
s = list(filter(lambda x: x[1] == 'Sun' and x[2] == 1,k))
k = list(filter(lambda x: x[4] > 1900,s))

print(len(k))
