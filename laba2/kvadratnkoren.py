import math

def formula (s, x):
    answer = (x + s / x) / 2
    while abs(x - answer) > 0.00001:
        x = answer
        answer = (x + (s / x)) / 2
    return answer

if __name__ == '__main__':
    s = float(input('Введите число корня: '))
    answer = formula(s, 3)

    print('Ответ = {}'.format(answer))
        input('Нажмите любую клавишу для выхода: ')
