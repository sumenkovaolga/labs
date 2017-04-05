def calculate():
    operation = str(input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    '''))
    a = int(input('Please enter the first number: '))
    b = int(input('Please enter the second number: '))
    if operation == '+':
        print('{} + {} = '.format(a, b))
        print(a + b)
    elif operation == '-':
        print('{} - {} = '.format(a, b))
        print(a - b)
    elif operation == '*':
        print('{} * {} = '.format(a, b))
        print(a * b)
    elif operation == '/':
        print('{} / {} = '.format(a, b))
        print(a / b)
    else:
        print('You have not typed a valid operator, please run the program again.')
    # Добавление функции again() в calculate()
    again()

def again():
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()
