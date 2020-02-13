from enum import Enum


class month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class season(Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4


flag = True
while flag == True:
    while True:
        try:
            s = month[input('month:')].value
            break
        except KeyError:
            print('Enter correct month')
    if s == 12 or s < 3:
        print('Winter')
    elif s < 6:
        print('Spring')
    elif s < 9:
        print('Summer')
    elif s < 12:
        print('Autumn')
    else:
        print('Невірно введений місяць')
    print(f'You want to continue?')
    text = input('')
    if text == 'yes':
        flag = True
    else:
        flag = False
