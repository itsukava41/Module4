def divide(first, second):
    try:
       result =  first / second
    except ZeroDivisionError:
        print('Error!')
    else:

        print(f'{first} / {second} =', result)