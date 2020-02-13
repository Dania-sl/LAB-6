flag = True
while flag == True:
    while True:
        try:
            x = int(input('Enter your time: '))
            break
        except ValueError:
            print('Enter correct time')

    color_time = x % 6
    if 0 <= color_time < 3:
        print('Green')
    elif 3 <= color_time < 4:
        print('Yellow')
    else:
        print('Red')
    print(f'You want to continue?')
    text = input('')
    if text == 'yes':
        flag = True
    else:
        flag = False
