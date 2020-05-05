# program to check if a year is leap year

year = int(input('Enter Year: '))

if year % 4 == 0:
    #print(year,'may be a leap year')
    if year % 100 == 0:
        if year % 400 ==0:
            print(year, 'is a leap year')
        else:
            print(year,'not a leap year')


    else:
        print(year,'is a leap year')


else:
    print(year,'not a leap year')