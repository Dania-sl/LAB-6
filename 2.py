from enum import Enum


class converter(Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4


flag = True
while flag == True:
    while True:
        try:
            x = float(input('AMOUNT OF MONEY:'))
            p = converter[input('currency:')]
            break
        except KeyError:
            print('Enter correct amount')
        except ValueError:
            print('Enter correct amount')
    if p == converter.USD:
        print(x / 24.58)
    elif p == converter.EUR:
        print(x / 26.9)
    elif p == converter.CZK:
        print(x / 1.08)
    elif p == converter.PLN:
        print(x / 6)
    else:
        print('Не вірне значення')
    print(f'You want to continue?')
    text = input('')
    if text == 'yes':
        flag = True
    else:
        flag = False
