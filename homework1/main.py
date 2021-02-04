#Prita Kapoor 8010339
print('Birthday Calculator')
print('Current day')
month = int(input('Month:'))
day = int(input('Day:'))
year = int(input('Year:'))
print('Birthday')
bmonth = int(input('Month:'))
bday = int(input('Day:'))
byear = int(input('Year:'))
year1 = abs(year - byear)
month1 = abs(month - bmonth)
day1 = abs(day - bday)
print('You are', year1, 'years old.')

if (month == bmonth) and (day == bday):
    print('Happy Birthday!')
