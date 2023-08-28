# Пользователь загадывает число от 0 до 1000 рандомно
# Программа должна за 10 попыток угадать его

from random import randint
LOW_LIMIT = 0
UP_LIMIT = 1000
num_run = randint(LOW_LIMIT, UP_LIMIT)

TRY_CASE_START = 1
TRY_CASE_STOP = 10
while TRY_CASE_START <= TRY_CASE_STOP:
    print('Попытка ', TRY_CASE_START, end='')
    user_number = int(input(' попробуй угадать число от 0 до 1000:'))
    if user_number == num_run:
        print('Угадали! Я загадал число ', num_run)
    elif user_number > num_run:
        print('Неа, я загадал меньшее число')
    else:
        print('Неа, я загадал большее число')
    TRY_CASE_START = TRY_CASE_START + 1
if user_number != num_run:
    print('Проиграл, я загадывал число ', num_run)