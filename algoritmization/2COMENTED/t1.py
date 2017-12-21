# Задание
# Напишите программу по заданному условию:
# Пользователь вводит число N, программа генерирует список из 10-ти случайных чисел, которые должны быть записаны на разных строчках в файле «output.txt»

import random # Включаем модуль случайных чисел

N = input('Введите порог N: ') # Запрос N у пользователя
N = int(N) # Преведение N из строки в целое число

FILE = open('output.txt', 'w') # Создание файла для вывода output.txt
LIST = [] # Введение переменной списка
LIST_STR = '' # Ввариант списка в текстовом формате для записи
for INDEX in range(0, 10): # Цикл 10 кратного нахождения случайного числа
    GEN_NUM = random.randrange(0, N) # Нах ождение рандомного числа в конкретном шаге цикла
    LIST.append(str(GEN_NUM)) # Добавляем в список число, тут же переведенное в строку
    LIST_STR = LIST_STR + str(GEN_NUM) + '\n' # Добавляем число к записуемому файлу, а также пропуск строки '\n'

FILE.write(LIST_STR) # Запись в файл буквенного варианта списка
FILE.close() # Окончание работы с файлом
print("Успешно!") # Поздравление с успешной операцией на сердце