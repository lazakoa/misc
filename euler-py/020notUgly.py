#!/bin/python
"""
    b) use the fact that 1 January 1555 was a saturday as reference. Write a
    code : input consists of three numbers: day, month and year (after 1 
    January 1555); output is the day of the week.
"""

def isLeapYear(n):
    if (n % 4 == 0):
        if (n % 100 == 0) and not(n % 400 == 0): 
            return False
        else:
            return  True
    else:
        return False

# february has 29 days instead of 28 on a leap year

def dayOfWeek(day,month,year):
    head = [365] # head, days left in 1555

    def tup(n):
        """ simple wrapper to make it easier to loop over the months"""
        return (n,n)
    
    # no typos below
    # february has 29 days instead of 28 on a leap year
    months = {   1: tup(31), #jan
                 2: (28,29), #feb
                 3: tup(31), #mar
                 4: tup(30), #apr
                 5: tup(31), #may
                 6: tup(30), #jun
                 7: tup(31), #jul
                 8: tup(31), #aug
                 9: tup(30), #sep
                10: tup(31), #oct
                11: tup(30), #nov
                12: tup(31), #dec
                }

    weekday = { 1: "sat",
                2: "sun",
                3: "mon",
                4: "tue",
                5: "wed",
                6: "thu", 
                0: "fri"}

    # works
    tail = [(months[i][0] if not(isLeapYear(year)) else months[i][1]) for i
            in range(1,month)] + [day] if month > 1 else [day]
            
    years = map(isLeapYear, range(1556, year))
    years = tail if year == 1555 else head + \
            list(map(lambda x: 366 if x else 365, years)) + \
            tail

    return weekday[sum(years) % 7]

if __name__ == '__main__':
    print(dayOfWeek(1,1,1555))
    print(dayOfWeek(1,1,2000))
    print(dayOfWeek(23,9,2016))
    print(dayOfWeek(27,9,2016))
    print(dayOfWeek(1,1,1600))
    print(dayOfWeek(19,10,2016))





