year = 2003
if year % 4 == 0 and year % 100 != 0:
    print('year is leap')
elif year % 400 == 0:
    print('year is leap')
else:
    print('regular year')
    
    
#2nd variant
if not year % 4 and not year % 100:
    print('year is leap')
elif not year % 400:
    print('year is leap')
else:
    print('regular year')