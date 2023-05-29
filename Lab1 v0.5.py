def is_int(char = ''):
    if len(char) == 1:
        try:
            char = int(char)
            return char
        except ValueError:
            print("Это не число")
    else:
        print("Это строка длинной минимум 2 символа")
            
while True:
    try:
        state = int(input("Выбери номер задачи(1 или 2) или отрицательное число для выхода:"))
    except ValueError:
        print("Это не число")
    if state == 1:
        print("Первое задание")
        char = is_int(input("Введите символ:"))
        print(type(char))
    elif state == 2:
        print("Второе задание")
    elif state < 0:
        break
    else:
        print("Число находится вне диапазона")
