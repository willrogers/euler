"""
Find the number of months in the twentieth century whose 
first day was a Sunday.
"""

reg_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 1900 wasn't a leap year.  2000 was.
# 1st Jan 1900 was a Monday = 1 (mod 7)
# We're looking for Sunday = 0 (mod 7)

day = 1 
# This gets us to 1st Jan 1901
day = (day + 365) % 7

no_suns = 0
for year in range(1901, 2001): 
    if (year % 4 == 0):
        this_year = leap_year
    else:
        this_year = reg_year

    for month in this_year:
        day = (day + month) % 7
        if day == 0:
            no_suns += 1

print(no_suns)
