## A game where you guess a random number or you input a number and the PC tries to guess it (it's not very hard)

import random, time, math
num_min = 0
num_max = 50
number = random.randint(num_min, num_max)
exit = False
tries = 6
n = tries


def replay(guessed, tries, n, number):
	exit_game = input(" Wanna play again? (Y/N)")
	if exit_game.upper() == "Y":
		n = tries
		number = random.randint(0, 50)
	elif exit_game.upper() == "N":
		n = tries
		guessed = True
	else:
		print("Write Y (yes) or N (no)")
	return guessed, n, number


def menu():
	menu = ""
	menu += "1.- Play\n"
	menu += "2.- Sim\n"
	menu += "3.- Exit\n"
	print(menu)
	option = int(input("Select an option: "))
	return option


def play_game(n, number):
	guessed = False
	while not guessed:
		try:
			tri = int(input("Write a number: "))
			n -= 1
			if tri == number:
				print("You won!")
				nt = tries - n
				print("You needed", nt, "tries")
				guessed, n, number = replay(guessed, tries, n, number)
			if tri < number:
				print("Bigger")
				print(n, "tries remaining")
			elif tri > number:
				print("Smaller")
				print(n, "tries remaining")
			if n == 0:
				print("You lost!")
				print("The number was", number)
				guessed, n, number = replay(guessed, tries, n, number)
		except ValueError:
			print("No se ha introducido un number")


def input_number():
	try:
		number = int(input(">>>"))
	except ValueError:
		print("A number wasn't written")
	tri = int((num_max - num_min)/2)
	max_try = num_max
	min_try = num_min
	return number, tri, max_try, min_try


def sim_game(n, number):
	guessed = False
	print("Intoduce a number for the machine to guess")
	number, tri, max_try, min_try = input_number()
	while not guessed:
		n -= 1
		print("\nMachine predicts...")
		time.sleep(3)
		print('\n{:^6}'.format(""))
		print('{:^6}'.format(tri))
		print('{:^6}\n'.format(""))
		if tri == number:
			print("The machine won")
			nt = tries - n
			print("It needed", nt, "tries")
			guessed, n, number = replay(guessed, tries, n, number)
			if not guessed:
					number, tri, max_try, min_try = input_number()
		if tri < number:
			min_try = tri
			tri = int(math.floor((max_try + min_try)/2))
			print("Bigger")
			print(n, "tries remaining")
			time.sleep(1)
		elif tri > number:
			max_try = tri
			tri = int(math.floor((max_try + min_try)/2))
			print("Smaller")
			print(n, "tries remaining")
			time.sleep(1)
		if n == 0:
			print("You won!")
			guessed, n, number = replay(guessed, tries, n, number)
while not exit:
	try:
		option = menu()
		if option == 1:
			play_game(n, number)
		elif option == 2:
			sim_game(n, number)
		elif option == 3:
			exit = True
		else:
			print("Insert a value inside the menu")
	except ValueError:
		print("Select an option of the menu")
	except KeyboardInterrupt:
		print("\nClosing program...")
		exit = True
