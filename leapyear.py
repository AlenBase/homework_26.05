print('Enter a year and I will output the number of leap years between the year entered and the year 1600.')
print('To exit the program, type \'q\'.')

while True:
    year_from_user = input('Enter year: ')
    if year_from_user == 'q':
        break
    try:
        year_from_user = int(year_from_user)
        count = 0
        if year_from_user > 1600:
            for year in range(1600, year_from_user + 1):
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    count += 1
        if year_from_user < 1600:
            for year in range(year_from_user, 1600 + 1):
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    count += 1
        print(f"Between 1600 and {year_from_user} year of {count} leap years.")
    except ValueError:
        print('Error. Enter only the year without words, and to exit the program, type \'q\'.')