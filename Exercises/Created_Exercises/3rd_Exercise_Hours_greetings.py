day_hour = input('Type the hour (0-24): ') # Getting the time

check_hour = (":" or ".") in day_hour
if check_hour == True:
    print(f'Daytime cannot have ":"/"." within')
else:
    alphabetic_hour = day_hour.isalpha()
    if alphabetic_hour == True:
        print('There is an alphabetic char within')
    else:
        daytime = int(day_hour)
        if 0 <= daytime <= 11:
            print('Good Morning!!!')
        elif 12 <= daytime <= 17:
            print('Godd Afternoon!!')
        else:
            print('Good Evening!!!')
