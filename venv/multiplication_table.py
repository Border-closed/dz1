#Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

i = 2
j = 2
table_stop_first = 10
table_stop_second = 11
while i < table_stop_first:
    while j < table_stop_second:
        result = i * j
        print(i, " * ", j, " = ", result)
        j = j + 1
    j = 2
    i = i + 1
    print()