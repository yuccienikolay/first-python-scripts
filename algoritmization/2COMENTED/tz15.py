# Задание
# Напишите программу по следующему условию:
# С клавиатуры вводится число N, необходимо вывести квадраты натуральных чисел, значение которых не будет больше произведения N на его половину. 

N = int(input("Число: ")) # Вводим число

for X in range(0, N): # Цикл проверяющий натуральные цисла 
	if X < N * (N / 2): # Функция логики проверяющая "значение которых не будет больше произведения N на его половину"
		print(X * X) # Вывод квадрата этого натурального числа